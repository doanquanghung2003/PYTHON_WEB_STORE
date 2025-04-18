from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

us_help_text='''
  <ul>
    <li>Bắt buộc.</li>
    <li>Tối đa 150 kí tự.</li>
  </ul>
'''

pass1_help_text='''
    <ul>
        <li>Mật khẩu không nên giống thông tin cá nhân</li>
        <li>Mật khẩu tối thiểu 8 kí tự</li>
        <li>Mật khẩu không quá phổ biến</li>
        <li>Mật khẩu có cả số và chữ</li>
    </ul>
'''
pass2_help_text='''
    Vui lòng nhập lại
'''
class BieuMau_DangKi_ThanhVien(UserCreationForm):
  email = forms.CharField(max_length=254, 
                          required=True, 
                          widget=forms.EmailInput(),
                          label='Thư điện tử')
  
  def __init__(self, *args, **kwargs):
    super(BieuMau_DangKi_ThanhVien, self).__init__(*args, **kwargs)
    
    self.fields['username'].label = "Tài khoản"
    self.fields['username'].help_text = us_help_text
    
    self.fields['password1'].label = "Mật khẩu"
    self.fields['password1'].help_text = pass1_help_text
    
    self.fields['password2'].label = "Xác nhận mật khẩu"
    self.fields['password2'].help_text = pass2_help_text
    
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
