# -*- coding: utf-8 -*-
# ==============================================================================
# filename          : storage.py
# email             : daniel@dqsdatalabs.com
# date              : 29.12.2022
# version           : 0.01
# ==============================================================================
        
        
import sqlite3
import pandas as pd
from ._config import DATABASE as DB
from ._config import TBL_DEBTORS, TBL_CREDITORS



class Storage:
    
    def __init__(self):
        """
        Initialize the repository
        """
        self.conn = sqlite3.connect(DB)
        
        
    def _create_table_debtors(self):
        """
        Create a table if it does not exist
        :param table_name: name of the table
        """
        
        columns = {
            'cnpj': 'text PRIMARY KEY', 
            'nome': 'text', 
            'nome_fantasia': 'text', 
            'valor_total_debito': 'real'
        }
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS {TBL_DEBTORS} ({', '.join(f'{k} {v}' for k,v in columns.items())})")
        self.conn.execute(f"CREATE UNIQUE INDEX IF NOT EXISTS idx_CNPJ ON {TBL_DEBTORS} (CNPJ)")
        self.conn.execute(f"CREATE INDEX IF NOT EXISTS idx_Nome ON {TBL_DEBTORS} (Nome)")
        

    def _save_dataframe(self, df:pd.DataFrame, table_name:str):
        """
        Save DataFrame to sqlite db
        :param df: DataFrame to save
        :param table_name: name of the table
        """
        
        try:
            df.to_sql(table_name, self.conn, if_exists='append', index=False, method='multi')
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")

    def _get_dataframe(self, table_name:str) -> pd.DataFrame:
        """
        Get DataFrame from sqlite db
        :param table_name: name of the table
        :return: DataFrame
        """
        return pd.read_sql_query(f"SELECT * FROM {table_name}", self.conn)
    
    def _get_debitors_by_cnpj(self, table_name:str, cnpj:str) -> pd.DataFrame:
        """
        Get DataFrame from sqlite db
        :param table_name: name of the table
        :param cnpj: CNPJ
        :return: DataFrame
        """
        return pd.read_sql_query(f"SELECT * FROM {table_name} WHERE CNPJ = '{cnpj}'", self.conn)
    
    def _export_to_excel(self, table_name:str, filename:str):
        """
        Export table to excel
        :param table_name: name of the table
        :param filename: name of the file
        """
        df = self.get_dataframe(table_name)
        df.to_excel(filename, index=False)

    def _close(self):
        """
        Close the connection to the db
        """
        self.conn.close()
        
    def save_debtors(self, df:pd.DataFrame):
        """
        Save DataFrame to sqlite db
        :param df: DataFrame to save
        """
        self._create_table_debtors()
        self._save_dataframe(df, TBL_DEBTORS)
        
    def save_creditors(self, df:pd.DataFrame):
        """
        Save DataFrame to sqlite db
        :param df: DataFrame to save
        """
        
        self._save_dataframe(df, TBL_CREDITORS)

    def get_debtors(self) -> pd.DataFrame:
        """
        Get DataFrame from sqlite db
        :return: DataFrame
        """
        return self._get_dataframe(TBL_DEBTORS)
    
    def get_creditors(self) -> pd.DataFrame:
        """
        Get DataFrame from sqlite db
        :return: DataFrame
        """
        return self._get_dataframe(TBL_CREDITORS)
    
    def get_debtor_by_cnpj(self, cnpj:str) -> pd.DataFrame:
        """
        Get DataFrame from sqlite db
        :param cnpj: CNPJ
        :return: DataFrame
        """
        return self._get_debitors_by_cnpj(TBL_DEBTORS, cnpj)
    
    def get_creditors_by_debtor_cnpj(self, cnpj:str) -> pd.DataFrame:
        """
        Get DataFrame from sqlite db
        :param cnpj: CNPJ
        :return: DataFrame
        """
        return self._get_debitors_by_cnpj(TBL_CREDITORS, cnpj)