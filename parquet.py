import pandas as pd
import glob
import os

def make_parquets():
    jsonl_files = glob.glob('chap*_dataset.jsonl')
    
    if not jsonl_files:
        print("[-] Files chap*_dataset.jsonl Not found in current dir")
        return

    all_dataframes = []
    required_columns = ['context', 'speaker', 'text']

    print(f"[*] Found files: {len(jsonl_files)}")

    for file_name in jsonl_files:
        try:
            df = pd.read_json(file_name, lines=True)
            
            df = df[required_columns]
            
            output_name = file_name.replace('.jsonl', '.parquet')
            df.to_parquet(output_name, index=False, engine='pyarrow')
            
            print(f"[+] Created: {output_name} ({len(df)} strings)")
            all_dataframes.append(df)
            
        except KeyError:
            print(f"[!] Error in {file_name}: missing required columns {required_columns}")
        except Exception as e:
            print(f"[!] Unable to process {file_name}: {e}")

    if all_dataframes:
        full_df = pd.concat(all_dataframes, ignore_index=True)
        full_df.to_parquet('full_chapters_dataset.parquet', index=False, engine='pyarrow')
        print(f"\n[OK] Main file ready: full_chapters_dataset.parquet ({len(full_df)} строк)")

if __name__ == "__main__":
    make_parquets()
