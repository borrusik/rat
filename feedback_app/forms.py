from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["professionalism", "clarity", "attitude", "comment"]

    professionalism = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Профессионализм (1-5)"
    )
    clarity = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Понятность объяснения (1-5)"
    )
    attitude = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Отношение к студентам (1-5)"
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False,
        label="Комментарий"
    )
