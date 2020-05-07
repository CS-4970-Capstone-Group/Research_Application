from research_gui import Research_Interface as view
import mysql.connector
#from heart_risk_classifier import Heart_Risk_Classifier as hc
from research_dbms import Research_DBMS as db
import tkinter as tk

class Controller(view):

    def run(self):
        view.init_interface(self)

    def create_connection(self):
        connection = None

        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="Catch_22#",
            database="research_dbms"
        )
        return connection

if __name__ == "__main__":
    controller = Controller()
    controller.run()