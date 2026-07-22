import stremlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการแปล",value=2569)
ce_year=bh_year-543
st.headar(f"ปี ค.ศ. คือ : {ce_year}")
