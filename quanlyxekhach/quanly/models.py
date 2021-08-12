from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/%Y/%m')


class LoaiXe(models.Model):
    tenLoaiXe = models.CharField(max_length=100, null=False, blank=False)
    soGhe = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.id)

class Xe(models.Model):
    soXe = models.CharField(max_length=6, null=False, blank=False, unique=True)
    tenLoaiXe = models.ForeignKey(LoaiXe, on_delete=models.SET_NULL, null=True, related_name="Xe_tenLoaiXe")

    def __str__(self):
        return str(self.id)

class Ghe(models.Model):
    tenGhe = models.CharField(max_length=4,blank=False,null=False, unique=True)
    trangThai = models.BooleanField(default=True)
    soXe = models.ForeignKey(LoaiXe, on_delete=models.SET_NULL, null=True, related_name="Ghe_soXe")
    def __str__(self):
        return self.tenGhe

class DiaDiem(models.Model):
    tenDiaDiem = models.CharField(max_length=150, blank=False, null=False, unique=True)

    def __str__(self):
        return self.tenDiaDiem

class TuyenXe(models.Model):
    diaDiemDi = models.ForeignKey(DiaDiem, on_delete=models.SET_NULL, null=True, related_name="TX_diaDiemDi")
    diaDiemDen = models.ForeignKey(DiaDiem, on_delete=models.SET_NULL, null=True, related_name="TX_diaDiemDen")

    def __str__(self):
        return str(self.id)

class BangGia(models.Model):
    giaVe = models.DecimalField(null=False, blank=False, default=0,decimal_places=0, max_digits=10)
    loaiXe = models.ForeignKey(LoaiXe,on_delete=models.SET_NULL, null=True, related_name="BG_loaiXe")
    tuyenXe = models.ForeignKey(TuyenXe,on_delete=models.SET_NULL, null= True, related_name="BG_tuyenXe")

    def __str__(self):
        return self.giaVe

class ChuyenXe(models.Model):
    thoiDiemKH = models.DateTimeField(null=False, blank=False)
    thoiGianHT = models.TimeField(null=False, blank=False)
    trangThai = models.BooleanField(default=True)
    soXe = models.ForeignKey(Xe, on_delete=models.SET_NULL, null=True, related_name="CX_soXe")
    maTaiXe = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="CX_maTaiXe")
    tuyenXe = models.ForeignKey(TuyenXe, on_delete=models.SET_NULL, null=True, related_name="CX_tuyenXe")

    def __str__(self):
        return str(self.id)

class PhanHoi(models.Model):
    noiDung = models.TextField()
    thoiGianTao = models.DateTimeField(auto_now_add=True)
    thoiGianCS = models.DateTimeField(auto_now=True)
    maKhachHang = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="PH_maKH")
    maChuyenXe = models.ForeignKey(ChuyenXe, on_delete=models.SET_NULL, null=True, related_name="PH_maChuyenXe")

    def __str__(self):
        return str(self.id)


class HinhThucTT(models.Model):
    tenHT = models.CharField(max_length=100, blank=False, null = False, unique=True)

    def __str__(self):
        return self.tenHT

class HoaDon(models.Model):
    ngayThanhToan = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    tongTien = models.DecimalField(default=0, null=False, blank = False,decimal_places=0, max_digits=10)
    hinhThuc  = models.ForeignKey(HinhThucTT, on_delete=models.SET_NULL, null=True, related_name="HD_hinhThuc")
    maKhachHang = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="HD_maKH")
    maNhanVien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="HD_maNV")

    def __str__(self):
        return str(self.id)

class ChiTietHoaDon(models.Model):
    maGhe = models.ForeignKey(Ghe, on_delete=models.SET_NULL, null=True, related_name="CTHD_maGhe")
    maChuyenXe = models.ForeignKey(ChuyenXe, on_delete=models.SET_NULL, null=True, related_name="CTHD_maChuyenXe")
    maHoaDon = models.ForeignKey(HoaDon, on_delete=models.SET_NULL, null=True, related_name="CTHD_maHoaDon")
    maGia = models.ForeignKey(BangGia, on_delete=models.SET_NULL, null=True, related_name="CTHD_maGia")

    def __str__(self):
        return str(self.id)

