import mysql.connector
import csv
import numpy as np
from matplotlib import pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)
from scipy import interpolate

class Research_DBMS():
    #BCG DBMS functions#----------------------------------

    def create_connection(self):
        connection = None

        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="Catch_22#",
            database="research_dbms"
            )
        return connection

    def convert_uscf_csv(self):
        with open(r"C:\Users\bradb\Documents\Research_Application\Log_to_CSV\REC0.LOG.csv", "r") as file:
            buffer = csv.reader(file)
            data_list = list(buffer)

        bcg_list = []
        time_list = []

        for i in range(len(data_list)):
            if(data_list[i][1] != ''):
                bcg_list.append(data_list[i][1])
                time_list.append(data_list[i][0])
        for j in range(3):
            bcg_list.remove(bcg_list[0])
            time_list.remove(time_list[0])

        for k in range(len(bcg_list)):
            if bcg_list[k] == '':
                bcg_list[k] = 0

        bcg_arr = np.array(bcg_list, dtype="double")
        time_arr = np.array(time_list, dtype="double")
        print(bcg_arr.size)
        xnew = np.arange(0, 30, .001)
        interpolation = interpolate.interp1d(time_arr, bcg_arr, fill_value="extrapolate", kind='cubic')
        x = np.linspace(0,30)
        results = interpolation(xnew)
        file.close()
        return results

    def convert_csv(self, directory):
        with open(directory, "r") as file:
            buffer = csv.reader(file)
            data_list = list(buffer)
        arr = np.array(data_list, dtype="double")
        bcg_arr = arr.flatten()
        file.close()
        return bcg_arr

    def create_bcg_records_table(self, entity, owner):
        print("creating table")
        sql = "CREATE TABLE IF NOT EXISTS " + entity + " (bcg_recording_id INT NOT NULL AUTO_INCREMENT, \
            classification_label INT, " + owner +  " INT NOT NULL, PRIMARY KEY (bcg_recording_id), \
            INDEX bcg_recording_idx (" + owner + " ASC) VISIBLE, CONSTRAINT " + owner + " FOREIGN KEY (" + owner + ") \
            REFERENCES people(person_id) ON DELETE CASCADE ON UPDATE CASCADE);"
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def create_bcg_data_table(self, entity, recordings_table, reference):
        print("creating bcg data table")
        print(reference)
        sql = "CREATE TABLE IF NOT EXISTS " + entity + " (bcg_data_id INT NOT NULL AUTO_INCREMENT, \
                bcg_data_value DOUBLE, " + reference + " INT NOT NULL, PRIMARY KEY (bcg_data_id), \
                INDEX bcg_data_idx (" + reference + " ASC) VISIBLE, CONSTRAINT " + reference + \
                " FOREIGN KEY (" + reference + ") REFERENCES " + recordings_table + " (bcg_recording_id) \
                ON DELETE CASCADE ON UPDATE CASCADE);"
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()

    #Primary Function (Use with GUI; includes form elements to take in directory to CSV and class and id of person)
    def insert_bcg_record(self, directory, class_label, person_id):
        conn = self.create_connection()
        cursor = conn.cursor()
        owner = "person_" + str(person_id) #naming convention for foreign key is just combo of person and id number
        records = "records_table_" + str(person_id) #based on naming convention for the table of records
        sql = "INSERT INTO " + records + " (classification_label, " + owner + ") VALUES (%s, %s);"
        print(sql)
        cursor.execute(sql, (class_label, person_id))
        #Setup for data table creation
        sql2 = "SELECT MAX(bcg_recording_id) FROM " +  records + ";"
        cursor.execute(sql2)
        id = cursor.fetchall()
        result_id = str(id[0][0])
        table_name = "bcg_table_" + result_id #unique data table name
        reference = "record_" + result_id #unique foreign key name
        conn.commit()
        cursor.close()
        conn.close()
        self.create_bcg_data_table(table_name, records, reference) #creating unique data table for individual record
        self.insert_bcg_data(directory, result_id, table_name) #populating/loading data into new unique data table

    #Primary Function (Use with GUI)
    def insert_person(self,age,gender,height,weight, bp,ht,gt,ethnicity,name):
        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO people (age, gender, height, weight, blood_pressure, hypertension, ground_truth_data, ethnicity, name) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (age,gender,height,weight,bp, ht, gt, ethnicity, name))
        #Setup for record table execution
        sql2 = "SELECT MAX(person_id) FROM people;"
        cursor.execute(sql2)
        id = cursor.fetchall()
        record_id = str(id[0][0])
        table_name = "records_table_" + record_id #naming convention for unique records table per person id
        owner = "person_" + record_id #naming convention for unique foreign key in the new records table
        conn.commit()
        cursor.close()
        conn.close()
        #Call to create the individual BCG records table
        self.create_bcg_records_table(table_name, owner)


    def insert_bcg_data(self, file_directory, record, table):
        data = self.convert_csv(file_directory)
        print(record)
        print(table)
        print("inserting bcg data")
        conn = self.create_connection()
        cursor = conn.cursor()
        foreign_key = "record_" + record
        print(foreign_key)
        sql = "INSERT INTO " + table + " (bcg_data_value, " + foreign_key + ") VALUES(%s, %s);"
        for i in range(len(data)):
            cursor.execute(sql, ((float(data[i])), record))
        conn.commit()
        cursor.close()
        conn.close()
     
     def insert_bcg_data_file(self, file_directory):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345678",
            database="GhostRiders"
            )
        # get cursor
        cursor = conn.cursor()
        sql_createTb = """create table bcg_table(
                health_data float,
                bcg_data_id int not null auto_increment,
                person_id int,
                primary key(bcg_data_id),
                foreign key(person_id) references people(subject_id));
                """
        cursor.execute(sql_createTb)
        csv_data = csv.reader(file_directory)
        for row in csv_data:
            cursor.execute('INSERT INTO bcg_table(health_data) VALUES ("%f")',row)
        conn.commit()
        cursor.close()
        conn.close()

    def delete_bcg_data(self):
        print("deleting bcg data")

    def delete_bcg_record(self):
        print("deleting bcg record")

    def review_table(self,table):
        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM " + table
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("reading table")
        for i in rows:
            print(rows)
        cursor.close()
        conn.close()

    def read_risk_and_age(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "SELECT age FROM people"
        cursor.execute(sql)
        ages = [ages[0] for ages in cursor.fetchall()]
        sql = "SELECT heart_failure_risk FROM people"
        cursor.execute(sql)
        risk = [risk[0] for risk in cursor.fetchall()]
        arr = []
        arr.append(ages)
        arr.append(risk)
        cursor.close()
        conn.close()
        return arr

    def update_classification(self, risk_level, person_id):
        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "UPDATE people SET heart_failure_risk = %s WHERE person_id = %s"
        cursor.execute(sql, (risk_level, person_id))
        conn.commit()
        cursor.close()
        conn.close()

    def read_classification(self, person_id):
        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "SELECT heart_failure_risk FROM people WHERE person_id = %s"
        cursor.execute(sql, (person_id))
        risk = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        print(risk)
        return risk

    #------------------------------------------------------
    #These functions may or may not be needed as the Keras library has some support for these kind of operations
    #CNN DBMS functions#-----------------------------------
    def update_kernel_weights(self):
        print("updating kernel weights")
        #read kernel size from respective kernel table
        #update kernel weights

    def update_fcl_weights(self):
        print("updating fully connected layer weights")

#Some on-the-fly testing
db = Research_DBMS()
dir = r"C:\Users\bradb\Documents\UCSF_Data_Processor\REC0_BCG.csv"
person = "subjectA"
#db.insert_person(20,"Male", 200, 180, 99, 0, 0, "African", "Subject0")
db.insert_bcg_record(dir, 1, 27)
#db.create_bcg_records_table(person)
#record = "subjecta_bcg_records"
#db.insert_bcg_record(record, 1, 0, 1)
#db.review_table(record)
#recording2 = "recording2"
#db.create_bcg_data_table(recording2, record)
#db.insert_bcg_data(dir, 11, recording2)
#db.read_risk_and_age()
#db.update_classification(0.5, 1)
#db.read_classification(4)


