#Định nghĩa một hàm có the tạo và in list chứa các giá trị bình phương của các so từ 1 đen 20 (tính cả 1 và 20). Sau đó thực thi hàm.

def ds_binh_phuong():
    ds = []
    for i in range(1, 21):
        ds.append(i * i)
    print(ds)