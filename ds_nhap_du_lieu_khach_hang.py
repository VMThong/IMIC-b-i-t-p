import pyodbc,re
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=LAPTOP-6GFL9EFK; DATABASE=QUAN_LY_LOP_HOC;Trusted_Connection=yes;')
cursor = conn.cursor()

print("Connect success")

#Table khách hàng
# tao_table_kh="""
# CREATE TABLE TABLE_KHACH_HANG1(
# MA_KHACH_HANG VARCHAR(50),
# TEN_KHACH_HANG NTEXT,
# DIEM_TICH_LUY INT,
# DIA_CHI_KHACH_HANG NTEXT,
# )
# """
#
# cursor.execute(tao_table_kh)
# cursor.commit()

#Viết thông tin từ đây input vào database
def them_khach_hang():
    MA_KHACH_HANG=input('Mã khách hàng là: ')
    TEN_KHACH_HANG=str(input('Tên khách hàng là: '))
    DIEM_TICH_LUY=input('Điểm tích lũy là: ')
    DIA_CHI_KHACH_HANG=str(input('Địa chỉ là: '))
    insert_data_table="""
    INSERT INTO TABLE_KHACH_HANG(MA_KHACH_HANG,TEN_KHACH_HANG,DIEM_TICH_LUY,DIA_CHI_KHACH_HANG)
    VALUES('"""+MA_KHACH_HANG+"""','"""+TEN_KHACH_HANG+"""',"""+DIEM_TICH_LUY+""",'"""+DIA_CHI_KHACH_HANG+"""');
    """
    print('đã chèn xong')
    cursor.execute(insert_data_table)
    cursor.commit()

#Cập nhận thông tin
def cap_nhat_thong_tin_KH():
    MA_KHACH_HANG_UP=input('Mã khách hàng là: ')
    TEN_KHACH_HANG_UP=str(input('Tên khách hàng mới là: '))
    DIEM_TICH_LUY_UP=input('Điểm tích lũy mới là: ')
    DIA_CHI_KHACH_HANG_UP=str(input('Địa chỉ mới là: '))

    update_data_table="""
    UPDATE TABLE_KHACH_HANG
    SET TEN_KHACH_HANG="""+TEN_KHACH_HANG_UP+""",DIEM_TICH_LUY="""+DIEM_TICH_LUY_UP+""",DIA_CHI_KHACH_HANG="""+DIA_CHI_KHACH_HANG_UP+"""
    WHERE MA_KHACH_HANG="""+MA_KHACH_HANG_UP+""";
    """
    print('đã cập nhật xong')
    cursor.execute(update_data_table)
    cursor.commit()

#Xóa khách hàng hoặc một loạt khách hàng
def delete_khach_hang():
    MA_KHACH_HANG_XOA=input('Mã khách hàng là: ')
    pt=','
    ngat_chuoi = re.split(pt, MA_KHACH_HANG_XOA)
    for i in ngat_chuoi:
        delete_data_table="""
        DELETE FROM TABLE_KHACH_HANG WHERE MA_KHACH_HANG="""+i+""";
        """
        cursor.execute(delete_data_table)
        cursor.commit()
    print('đã xóa xong')

#Lấy thông tin khách hàng
def lay_thong_tin_KH():
    MA_KHACH_HANG_INFO=input('Mã khách hàng là: ')
    lay_data_table="""
    SELECT *
    FROM TABLE_KHACH_HANG
    WHERE MA_KHACH_HANG="""+MA_KHACH_HANG_INFO+""";
    """
    data=cursor.execute(lay_data_table)
    thong_tin=data.fetchall()
    print(thong_tin)
    print('đã lấy thông tin xong')

a= them_khach_hang()


