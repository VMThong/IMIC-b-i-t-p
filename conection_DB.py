import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=LAPTOP-6GFL9EFK; DATABASE=QUAN_LY_LOP_HOC;Trusted_Connection=yes;')
cursor = conn.cursor()

print("Connect success")

#Tạo table bên sever SQL bằng python, lệnh trong tao_table là lệnh SQL không phải lệnh python
# tao_table="""
# CREATE TABLE QUAN_LY_LOP_HOC(
# MA_LOP_HOC VARCHAR(50),
# TEN_LOP_HOC VARCHAR(100),
# GHI_CHU NVARCHAR(500),
# SO_LUONG_HOC_VIEN INT
# )
# """
#
# cursor.execute(tao_table)
# cursor.commit()

#Chèn dữ liệu vào table
# insert_data_table="""
# INSERT INTO LOP_HOC(MA_LOP_HOC,TEN_LOP_HOC,GHI_CHU,SO_LUONG_HOC_VIEN)
# VALUES ('004','A3','','30'),('005','A2','','24'),('006','A7','','31')
#
# """
# print('đã chèn xong')
# cursor.execute(insert_data_table)
# cursor.commit()

#Lấy dữ liệu từ table bằng select
select_data_tu_database="""
SELECT *
FROM LOP_HOC
"""
data= cursor.execute(select_data_tu_database)
ds_lop_hoc=data.fetchall()
print(ds_lop_hoc)
print(ds_lop_hoc[0][0])
