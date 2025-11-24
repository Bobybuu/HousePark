# 🤝 Contributing to HousePark

Thank you for your interest in contributing to HousePark! We welcome contributions from the community and are excited to collaborate with you.

## 📞 Contact for Contributions

**Before making significant changes, please contact us:**

- **Email:** 📧 `c43057772@gmail.com`
- **WhatsApp:** 📱 `+254703274032`
- **Response Time:** Within 24-48 hours

## 🎯 Contribution Workflow

### 1. **Pre-Contribution Steps**
```bash
# Fork the repository
# Clone your fork
git clone https://github.com/YOUR_USERNAME/HousePark.git
cd HousePark

# Create  feature branch
git checkout -b feature/your-feature-name
```

### 2. **Discussion First**
- **Small fixes:** Direct pull requests are welcome
- **New features:** Contact us first for discussion
- **Major changes:** Requires design approval before implementation

### 3. **Development Rules**

#### 🐍 **Python/Django Standards**
```python
# ✅ Good
class UserProfileView(APIView):
    """User profile management endpoint."""
    
    def get(self, request):
        """Retrieve user profile data."""
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

# ❌ Avoid
class userProfile(APIView):
    def get(self, req):
        u = req.user
        s = UserProfileSerializer(u)
        return Response(s.data)
```

#### 📁 **Code Organization**
```
housepark/
├── server/
│   ├── apps/
│   │   ├── users/           # Authentication & profiles
│   │   ├── properties/      # Property listings
│   │   ├── inquiries/       # Contact forms
│   │   └── management/      # Property management
│   └── config/              # Project settings
```

### 4. **Commit Message Convention**
```bash
# Format: type(scope): description

# Examples:
git commit -m "feat(auth): add email verification system"
git commit -m "fix(properties): resolve image upload issue"
git commit -m "docs(readme): update installation instructions"
git commit -m "test(users): add user registration tests"
git commit -m "refactor(admin): improve jazzmin configuration"
```

**Commit Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### 5. **Pull Request Process**

#### **PR Checklist:**
- [ ] **Contacted maintainers** for major features
- [ ] **Tests added/updated** for new functionality
- [ ] **Documentation updated** (README, docstrings)
- [ ] **Code follows style guidelines**
- [ ] **No breaking changes** without discussion
- [ ] **Commit messages** follow convention

#### **PR Template:**
```markdown
## Description
Brief description of the changes...

## Related Issues
Fixes #issue_number

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactor

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
```

## 🛠️ Development Setup

### **Backend Requirements**
```bash
# Python 3.8+
python --version

# PostgreSQL
psql --version

# Install dependencies
pip install -r requirements.txt

# Environment setup
cp .env.example .env
# Edit .env with your local settings

# Database setup
python manage.py migrate
python manage.py createsuperuser
```

### **Code Quality Standards**

#### **Python/Django**
```bash
# Run code formatting
black server/

# Check code style
flake8 server/

# Run tests
python manage.py test

# Check migrations
python manage.py makemigrations --check
```

#### **Security Guidelines**
- Never commit sensitive data (API keys, passwords)
- Use environment variables for configuration
- Validate all user inputs
- Follow Django security best practices

## 🚫 Contribution Restrictions

### **Do Not:**
- ❌ **Modify core architecture** without discussion
- ❌ **Add major dependencies** without approval
- ❌ **Change database schema** breaking existing data
- ❌ **Remove features** without deprecation period
- ❌ **Commit directly to main branch**

### **Requires Approval:**
- 🔒 **New user roles** or permission changes
- 🔒 **Payment integration** changes
- 🔒 **Third-party API integrations**
- 🔒 **Database schema modifications**
- 🔒 **Authentication system changes**

## 🐛 Bug Reports

### **Bug Report Template:**
```markdown
## Description
Clear description of the bug...

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen...

## Actual Behavior
What actually happens...

## Environment
- OS: [e.g., Windows, macOS]
- Python Version: [e.g., 3.9.7]
- Django Version: [e.g., 5.2.8]
- Browser: [if applicable]

## Screenshots/Logs
[Attach relevant screenshots or error logs]
```

## 💡 Feature Requests

### **Feature Proposal Template:**
```markdown
## Problem Statement
What problem does this feature solve?

## Proposed Solution
How should the feature work?

## Alternative Solutions
Any other approaches considered?

## Additional Context
Screenshots, mockups, or references
```

## 📋 Code Review Process

### **What We Look For:**
1. **Code Quality**
   - Follows Django/Python best practices
   - Proper error handling
   - Clean, readable code

2. **Functionality**
   - Solves the intended problem
   - No breaking changes
   - Proper test coverage

3. **Documentation**
   - Clear docstrings
   - Updated README if needed
   - API documentation

4. **Security**
   - No security vulnerabilities
   - Proper input validation
   - Secure authentication flows

### **Review Timeline:**
- **Small changes:** 1-3 days
- **Medium features:** 3-7 days  
- **Major contributions:** 1-2 weeks

## 🏆 Recognition

### **Contributor Tiers:**
- **🌱 Beginner:** First successful contribution
- **🚀 Regular:** Multiple quality contributions
- **🌟 Core:** Significant feature additions
- **🏆 Maintainer:** Long-term project commitment

### **Recognition Includes:**
- Contributor shoutouts in README
- Project role opportunities
- Feature naming rights for major contributions
- Potential maintainer status

## 📄 License Agreement

By contributing to HousePark, you agree:
- Your contributions will be licensed under AGPLv3
- You have the right to submit the code
- You grant project maintainers license to use your contributions

## 🆘 Getting Help

### **Quick Questions:**
- **WhatsApp:** `+254703274032` (Development discussions)
- **Email:** `c43057772@gmail.com` (Formal proposals)

### **Response Times:**
- **Urgent issues:** 2-12 hours
- **Feature requests:** 24-48 hours
- **Major proposals:** 3-5 days

## 🙏 Thank You!

We appreciate every contribution, no matter how small. Together we can build an amazing real estate platform! 🏠✨

---

*Last updated: $(date)*  
*Maintainer: Chrispin Odiwuor*