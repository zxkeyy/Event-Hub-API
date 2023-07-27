from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_mb = 2

    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f'File is larger than {max_size_mb}MB')