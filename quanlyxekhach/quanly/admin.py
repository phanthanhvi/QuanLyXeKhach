from django.contrib import admin
from .models import *



class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'is_active']

class LoaiXeAdmin(admin.ModelAdmin):
    list_display = ['tenLoaiXe', 'soGhe']

class XeAdmin(admin.ModelAdmin):
    list_display = ['soXe', 'tenLoaiXe']

class GheAdmin(admin.ModelAdmin):
    list_display = ['tenGhe','trangThai','soXe']

class DiaDiemAdmin(admin.ModelAdmin):
    list_display = ['tenDiaDiem']

class TuyenXeAdmin(admin.ModelAdmin):
    list_display = ['diaDiemDen','diaDiemDi']

class BangGiaAdmin(admin.ModelAdmin):
    list_display = ['giaVe','loaiXe', 'tuyenXe']


class ChuyenXeAdmin(admin.ModelAdmin):
    list_display = ['thoiDiemKH','thoiGianHT','trangThai','soXe','maTaiXe','tuyenXe']

class PhanHoiAdmin(admin.ModelAdmin):
    list_display = ['noiDung','thoiGianTao','thoiGianCS','maKhachHang','maChuyenXe']


class HinhThucAdmin(admin.ModelAdmin):
    list_display = ['tenHT']

class HoaDonAdmin(admin.ModelAdmin):
    list_display = ['ngayThanhToan','tongTien','hinhThuc','maKhachHang','maNhanVien']

class CTHDAdmin(admin.ModelAdmin):
    list_display = ['maGhe','maChuyenXe','maHoaDon','maGia']

admin.site.register(User,UserAdmin)
admin.site.register(LoaiXe,LoaiXeAdmin)
admin.site.register(Xe, XeAdmin)
admin.site.register(Ghe, GheAdmin)
admin.site.register(DiaDiem, DiaDiemAdmin)
admin.site.register(TuyenXe, TuyenXeAdmin)
admin.site.register(ChuyenXe, ChuyenXeAdmin)
admin.site.register(BangGia, BangGiaAdmin)
admin.site.register(PhanHoi, PhanHoiAdmin)
admin.site.register(HinhThucTT, HinhThucAdmin)
admin.site.register(HoaDon, HoaDonAdmin)
admin.site.register(ChiTietHoaDon,CTHDAdmin)
