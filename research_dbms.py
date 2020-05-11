import mysql.connector
import csv
import numpy as np
from matplotlib import pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)
from scipy import interpolate
from tkinter import messagebox

class Research_DBMS():
    #BCG DBMS functions#----------------------------------
    def create_connection(self):
        connection = None
        '''
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="Catch_22#",
            database="research_dbms"
            )
        return connection
        '''
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345678",
            database="GhostRiders"
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
    
    def create_bcg_records_table(self, entity):
        print("creating table")
        sql = "CREATE TABLE IF NOT EXISTS " + entity + "_bcg_records (bcg_recording_id INT NOT NULL AUTO_INCREMENT, \
            has_ground_truth INT, classification_label INT, owner_id INT NOT NULL, PRIMARY KEY (bcg_recording_id), \
            INDEX bcg_recording_idx (owner_id ASC) VISIBLE, CONSTRAINT owner_id FOREIGN KEY (owner_id) \
            REFERENCES people(person_id) ON DELETE CASCADE ON UPDATE CASCADE);"
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()

    def create_bcg_data_table(self, entity, recordings_table):
        print("creating bcg data table")
        sql = "CREATE TABLE IF NOT EXISTS " + entity + " (bcg_data_id INT NOT NULL AUTO_INCREMENT, \
                bcg_data_value DOUBLE, recording_id2 INT NOT NULL, PRIMARY KEY (bcg_data_id), \
                INDEX bcg_data_idx (recording_id2 ASC) VISIBLE, CONSTRAINT recording_id2 \
                FOREIGN KEY (recording_id2) REFERENCES " + recordings_table + "(bcg_recording_id) \
                ON DELETE CASCADE ON UPDATE CASCADE);"
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()

    def insert_bcg_record(self, records, ground_truth, class_label, owner_id):
        if ground_truth != 1 or ground_truth != 0:
            print("Invalid Ground Truth Entry")

        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO " + records + " (has_ground_truth, classification_label, owner_id) VALUES (%s, %s, %s);"
        cursor.execute(sql, (ground_truth, class_label, owner_id))
        conn.commit()
        cursor.close()
        conn.close()

    def insert_person(self, name, height, weight, age, bloodh, bloodl, ethnicity, gender, hypertension, ground_truth):

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345678",
            database="GhostRiders"
            )
        #get cursor
        cursor = conn.cursor()
        sql = "INSERT INTO people(name,height,weight,age,blood_pressure_high,blood_pressure_low,ethnicity,gender,hypertension,ground_truth) VALUES ('%s','%s','%s', '%s', '%s','%s','%s', '%s','%s','%s')" % (name, height, weight, age, bloodh, bloodl, ethnicity, gender, hypertension, ground_truth)
        try:
            #execute the sql command
            cursor.execute(sql)
            print("Insert the data successfully")
            #submit to the database
            conn.commit()
            messagebox.showinfo("INFO", "Successfully Insert")
        except:
            print("Insert the data fail")
            messagebox.showinfo(("INFO", "Failed to insert"))
            #Rollback in case there is any error
            conn.rollback()
        cursor.close()
        conn.close()
    
    def insert_person_clear(self,entry_name, entry_height, entry_weight, entry_age,entry_blood_pressure_high, entry_blood_pressure_low,ethnicitychoosen,gender_choosen,hypertension_choosen,ground_truth_choosen):
        END = 'end'
        entry_name.delete(0,END)
        entry_height.delete(0,END)
        entry_weight.delete(0,END)
        entry_age.delete(0,END)
        entry_blood_pressure_high.delete(0,END)
        entry_blood_pressure_low.delete(0,END)
        ethnicitychoosen.delete(0,END)
        gender_choosen.delete(0,END)
        hypertension_choosen.delete(0,END)
        ground_truth_choosen.delete(0,END)

    def insert_bcg_data(self, file_directory, record, table):
        data = self.convert_csv(file_directory)
        print("inserting bcg data")
        conn = self.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO " + table + " (bcg_data_value, recording_id2) VALUES (%s, %s)"
        for i in range(len(data)):
            cursor.execute(sql, (float(data[i]), record))
        conn.commit()
        cursor.close()
        conn.close()
    
    def search_person(self, searchid):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345678",
            database="GhostRiders"
            )
        # get cursor
        cursor = conn.cursor()
        # SQL insert command
        sql = "SELECT * FROM  people WHERE subject_id = '%s' " % (searchid)
        try:
            # execute the sql command
            cursor.execute(sql)
            temp = cursor.fetchall()
            # submit to the database
            conn.commit()
            for i, item in enumerate(temp):
                self.treeAddressList.insert('', i, values=item[1:])
            print("search the data successfully")
        except:
            print("search the data fail")
            # Rollback in case there is any error
            messagebox.showinfo("INFO", "Failed to Search")
            conn.rollback()
        cursor.close()
        # Close the database
        conn.close()

    def search_person_clear(self,entry_subject_id):
        END = 'end'
        entry_subject_id.delete(0,END)
    
    def delete_person(self, inputid):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345678",
            database="GhostRiders"
            )
        # get cursor
        cursor = conn.cursor()
        # SQL insert command
        sql = "DELETE FROM people WHERE subject_id = '%s' " % (inputid)
        try:
            # execute the sql command
            cursor.execute(sql)
            print("delete the data successfully")
            # submit to the database
            conn.commit()
            messagebox.showinfo("INFO", "Successfully delete")
        except:
            print("delete the data fail")
            # Rollback in case there is any error
            messagebox.showinfo("INFO", "Failed to delete")
            conn.rollback()
        cursor.close()
        # Close the database
        conn.close()

    def delete_person_clear(self,entry_id_to_delete):
        END = 'end'
        entry_id_to_delete.delete(0,END)

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

    def dbage():
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345678",
            database="GhostRiders"
            )
        # get cursor
        cursor = conn.cursor()
        # SQL insert command
        sql = "SELECT age FROM people"
        try:
            # execute the sql command
            cursor.execute(sql)
            temp = cursor.fetchall()
            print("select age successful")
            datalist = []
            for age in temp:
                datalist.append(age[0])
            
            # submit to the database
            conn.commit()
        except:
            print("retrieve the data fail")
            # Rollback in case there is any error
            messagebox.showinfo("INFO", "Failed to retrive")
            conn.rollback()
        # Close the database
        return datalist
        conn.close()

    def dbweight():
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345678",
            database="GhostRiders"
            )
        # get cursor
        cursor = conn.cursor()
        # SQL insert command
        sql = "SELECT weight FROM people"
        try:
            # execute the sql command
            cursor.execute(sql)
            temp = cursor.fetchall()
            print("select weight successful")
            datalist = []
            for weight in temp:
                datalist.append(weight[0])
            
            # submit to the database
            conn.commit()
        except:
            print("retrieve the data fail")
            # Rollback in case there is any error
            messagebox.showinfo("INFO", "Failed to retrive")
            conn.rollback()
        # Close the database
        return datalist
        conn.close()

    def dbbmi():
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345678",
            database="GhostRiders"
            )
        # get cursor
        cursor = conn.cursor()
        # SQL insert command
        sql = "SELECT weight FROM people"
        try:
            # execute the sql command
            cursor.execute(sql)
            temp = cursor.fetchall()
            print("select weight successful")
            datalist_weight = []
            for weight in temp:
                datalist_weight.append(weight[0])
            
            # submit to the database
            conn.commit()
        except:
            print("retrieve the data fail")
            # Rollback in case there is any error
            messagebox.showinfo("INFO", "Failed to retrive")
            conn.rollback()
        # Close the database
        sql = "SELECT height FROM people"
        try:
            # execute the sql command
            cursor.execute(sql)
            temp = cursor.fetchall()
            print("select height successful")
            datalist_height = []
            for height in temp:
                datalist_height.append(height[0])
            
            # submit to the database
            conn.commit()
        except:
            print("retrieve the data fail")
            # Rollback in case there is any error
            messagebox.showinfo("INFO", "Failed to retrive")
            conn.rollback()
        array = np.array(datalist_height)
        array_cm = array/100.
        datalist_height_new = list(array_cm)
        bmi = [a/(b**2) for a,b in  zip(datalist_weight,datalist_height_new)]     
        return bmi
        conn.close()

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
#dir = r"C:\Users\bradb\Documents\UCSF_Data_Processor\REC0_BCG.csv"
person = "subjectA"
#db.create_bcg_records_table(person)
#record = "subjecta_bcg_records"
#db.insert_bcg_record(record, 1, 0, 1)
#db.review_table(record)
#recording2 = "recording2"
#db.create_bcg_data_table(recording2, record)
#db.insert_bcg_data(dir, 11, recording2)
db.read_risk_and_age()
#db.update_classification(0.5, 1)
#db.read_classification(4)


