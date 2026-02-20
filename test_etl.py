from etl import extract
import pandas as pd
from io import StringIO

TEST_CSV = StringIO("""customer_name,quantity,unit_price
Ahmed,2,100
""")

def test_extract():
    df = extract(csv_path=TEST_CSV)
    
    assert len(df) == 1
    
    assert "customer_name" in df.columns
    assert "quantity" in df.columns
    assert "unit_price" in df.columns
    
    assert df.iloc[0]["customer_name"] == "Ahmed"
    assert df.iloc[0]["quantity"] == 2
    assert df.iloc[0]["unit_price"] == 100