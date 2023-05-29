# C R U D
# Create
# Read
# Update

from PTTC1dinhnghia import PTTC1

class Quanlyhocvien:
    list_hocvien = []
    
    def themhocvien(self): # self bien goi ham
        n = int(input("Nhap so luong hoc vien: "))
        for i in range(1,n+1):
            print("Nhap hoc vien thu {}".format(i))
            ten = input("Nhap ten {} :  ".format(i))
            tuoi = int(input("Nhap tuoi: "))
            quequan = input("Nhap que quan: ")
            lop = input("Nhap lop: ")
            tienganh = float(input("Nhap diem tieng anh: "))
            tinhoc = float(input("Nhap diem tin hoc:  "))
            diemtrungbinh = float((tienganh + tinhoc)/2)
            hocvien = PTTC1(ten,tuoi,quequan,lop,tienganh,tinhoc) #ten tuoi que quan la key 
            if(diemtrungbinh>5):
                hocvien.xeploai = "Gioi" # cham vao la them vao
            else:
                hocvien.xeploai = "Yeu"
            
            hocvien.id = i

            self.list_hocvien.append(hocvien)

        
    

    def hienthihocvien(self):
        print ("{:<8} {:<8} {:<8} {:<8} {:<8}{:<8}{:<8}{:<8}".format("ID","Ten","Tuoi","QueQuan ","Lop"," TiengAnh ","TinHoc "," Xeploai"))
        for i in self.list_hocvien:
            print("{:<8} {:<8} {:<8} {:<8} {:<8}{:<8}{:<8}{:<8}".format(i.id,i.ten,i.tuoi,i.quequan,i.lop,i.tienganh,i.tinhoc,i.xeploai))

    def sua_thong_tin_hv(self,hocvien_id):
        for hocvien in self.list_hocvien:
            if hocvien.id == hocvien_id:
                tenmoi = input("nhap ten can sua: ")
                tuoimoi = int(input("nhap tuoi can sua: "))
                hocvien.ten = tenmoi
                hocvien.tuoi = tuoimoi
                print("thong tin hoc vien da duoc cap nhat")
                self.hienthihocvien()
                return
        print("khong tim thay id")
        



test = Quanlyhocvien()
test.themhocvien()
test.hienthihocvien()

hocvien_id = int(input("nhap ID hoc vien: "))
test.sua_thong_tin_hv(hocvien_id)
