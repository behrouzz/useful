import os
import glob


def split_file(input_file_path, chunk_size_mb=9):
    """
    Split a large file into smaller chunks in the Databricks workspace.
    
    Args:
        input_file_path (str): Path to the input file (e.g., '/Workspace/Users/your_username/my_sqlite_database.db')
        chunk_size_mb (int): Size of each chunk in MB (default: 9 MB to stay under 10 MB limit)
    
    Returns:
        list: List of output file paths
    """
    chunk_size = chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    output_files = []
    part_number = 0
    
    try:
        with open(input_file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:  # End of file
                    break
                # Generate output file path (e.g., my_sqlite_database.db.part0)
                output_file = f"{input_file_path}.part{part_number}"
                with open(output_file, 'wb') as out_f:
                    out_f.write(chunk)
                output_files.append(output_file)
                print(f"Created {output_file} ({len(chunk)} bytes)")
                part_number += 1
        
        print(f"Split {input_file_path} into {len(output_files)} parts")
        return output_files
    
    except Exception as e:
        print(f"Error splitting file: {e}")
        return []



def merge_files(input_pattern, output_file):
    """
    Merge split files into a single file.
    
    Args:
        input_pattern (str): Glob pattern for split files (e.g., 'my_sqlite_database.db.part*')
        output_file (str): Path to the output file (e.g., 'my_sqlite_database.db')
    
    Returns:
        bool: True if successful, False if failed
    """
    try:
        # Get list of part files, sorted by part number
        part_files = sorted(glob.glob(input_pattern), key=lambda x: int(x.split('.part')[-1]))
        if not part_files:
            print("No part files found")
            return False
        
        with open(output_file, 'wb') as out_f:
            for part_file in part_files:
                print(f"Merging {part_file}")
                with open(part_file, 'rb') as in_f:
                    out_f.write(in_f.read())
        
        print(f"Merged {len(part_files)} parts into {output_file} ({os.path.getsize(output_file)} bytes)")
        return True
    
    except Exception as e:
        print(f"Error merging files: {e}")
        return False
