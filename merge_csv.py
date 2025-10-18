import csv
import os
import glob

def merge_all_csv_files():
    """Merge all individual comment CSV files into one result.csv with 20,000 rows."""
    
    # Find all CSV files matching the pattern comments_*.csv
    csv_files = glob.glob("comments_*.csv")
    
    if not csv_files:
        print("No CSV files found matching pattern 'comments_*.csv'")
        return
    
    print(f"\nFound {len(csv_files)} CSV files to merge")
    print("="*70)
    
    all_comments = []
    
    # Read all comments from individual CSV files
    for csv_file in csv_files:
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                
                for row in reader:
                    if row and row[0].strip():  # Only add non-empty comments
                        all_comments.append(row[0].strip())
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")
    
    print(f"\nTotal comments collected: {len(all_comments):,}")
    
    # Limit to exactly 20,000 comments
    if len(all_comments) > 20000:
        all_comments = all_comments[:20000]
        print(f"Trimmed to: 20,000 comments")
    else:
        print(f"Note: Only {len(all_comments):,} comments available (less than 20,000)")
    
    # Write to result.csv
    output_file = "result.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Comment"])  # Header row
        
        for comment in all_comments:
            writer.writerow([comment])
    
    print("="*70)
    print(f"\n✅ SUCCESS!")
    print(f"   Output file: {output_file}")
    print(f"   Total rows: {len(all_comments):,} (including header)")
    print(f"   Columns: 1 (Comment)")
    print(f"   All individual CSV files have been merged")
    print("="*70)

if __name__ == "__main__":
    merge_all_csv_files()
