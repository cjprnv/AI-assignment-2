import random
import string

# -------------------------------
# CAPTCHA Generator
# -------------------------------

class CaptchaGenerator:
    def generate_captcha(self, length=6):
        characters = string.ascii_letters + string.digits
        captcha = ''.join(random.choice(characters) for _ in range(length))
        return captcha


# -------------------------------
# CAPTCHA Validator
# -------------------------------

class CaptchaValidator:
    def validate(self, generated, user_input):
        return generated == user_input


# -------------------------------
# Controller
# -------------------------------

def run_captcha():
    generator = CaptchaGenerator()
    validator = CaptchaValidator()

    captcha = generator.generate_captcha()
    print("CAPTCHA:", captcha)

    user_input = input("Enter CAPTCHA: ")

    if validator.validate(captcha, user_input):
        print("Access Granted ✅")
    else:
        print("Access Denied ❌")


if __name__ == "__main__":
    run_captcha()