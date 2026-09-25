import pandas as pd

class AnimeDataLoader :
    def __init__(self,original_csv:str,processed_csv:str) :
        self.original_csv=original_csv
        self.processed_csv=processed_csv
        
    def load_and_process(self) :
        df= pd.read_csv(self.original_csv , encoding='utf-8') .dropna()
        
        required_column={'Name','Genres','sypnopsis'}
        
        missing = required_column - set(df.columns)
        
        if missing :
            raise ValueError("Missing Column in csv file")
        
        df['combined_info'] =(
            "Title:" + df["Name"]+" overview :" + df["sypnopsis"] +" Genres: "+  df["Genres"]
        )
        
        df[['combined_info']].to_csv(self.processed_csv , index=False, encoding='utf-8') 
         
        return self.processed_csv
           
        