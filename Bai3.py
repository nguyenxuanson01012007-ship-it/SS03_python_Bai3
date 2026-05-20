    for i in range(1,4):
    print("Thông tin của nhân viết thứ: ", i)
    number_id = int(input("Mã nhân viên: "))
    full_name = input("Họ và tên nhân viên: ")
    department = input("Phòng ban công tác: ")

    if number_id == " " or (full_name == " "):
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        continue

    print("\n--- Phiếu Hồ sơ Điện tử ----")
    print("Mã nhân viên: ", number_id)
    print("Họ và tên nhân viên: ", full_name)
    print("Phòng ban công tác: ", number_id)
    print("----------------------------\n")

print("Đã hoàn tất quá trình duyệt thường cho 3 nhân viên!")

    
