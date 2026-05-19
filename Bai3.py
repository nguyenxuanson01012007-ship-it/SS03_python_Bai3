print('Khởi tạo hồ sơ nhân sự');
employees = [];
for employee in range(1,4):
    print('Thông tin nhân viên ', employee);
    id_emp = input('Nhập mã nhân viên: ');
    name_emp = input('Nhập tên nhân viên: ');
    dept_emp = input('Nhập phòng ban nhân viên: ');
    employees.append({
        'id' : id_emp,
        'name' : name_emp,
        'dept' : dept_emp
    })

if id_emp =="" or name_emp == "" : 
    print ("[CANH BAO] Dữ Liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")

else :

    print('Hồ sơ sau khi tiếp nhận');
    for emp in employees:
        print('Mã nhân viên là: ', emp['id']);
        print('Tên nhân viên là: ', emp['name']);
        print('Phòng ban nhân viên là: ', emp['dept']);
