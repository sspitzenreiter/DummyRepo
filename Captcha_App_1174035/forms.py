from django import forms
from Captcha_App_1174035.models import User
from captcha.fields import CaptchaField


class UserForm(forms.ModelForm):
	captcha = CaptchaField()

	def clean(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError("Password tidak sesuai")

		email = self.cleaned_data.get('email')
		email_data = User.objects.filter(email=email)
		if email_data.exists():
			raise forms.ValidationError("Email sudah ada yang memakai")

		norek = self.cleaned_data.get('norek')
		if norek == "":
			raise forms.ValidationError("Nomor rekening tidak boleh kosong")

		namarekening = self.cleaned_data.get('namarekening')
		if namarekening == "":
			raise forms.ValidationError("Nama rekening tidak boleh kosong")

		nama_bank = self.cleaned_data.get('nama_bank')
		if nama_bank == "":
			raise forms.ValidationError("Bank tidak bole kosong")
	class Meta:
		model = User
		fields = '__all__'
		widgets = {
			'password': forms.PasswordInput(),
			'confirm_password':forms.PasswordInput()
		}
		