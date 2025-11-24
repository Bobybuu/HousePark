# 🏠 HousePark - Modern Real Estate Platform

![Django](https://img.shields.io/badge/Django-5.2.8-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![React](https://img.shields.io/badge/React-18-cyan)
![Mapbox](https://img.shields.io/badge/Mapbox-GL-orange)
![License](https://img.shields.io/badge/License-AGPLv3-red)

A comprehensive real estate platform connecting buyers, sellers, and agents with advanced property search, management tools, and seamless user experiences.

## ✨ Features

### 🏡 Property Management
- **Multi-type Listings**: Land, Commercial, Rental, Apartment, For Sale
- **Advanced Search**: Location-based with Mapbox integration
- **Image Galleries**: High-quality property photos with zoom
- **Smart Filters**: Price, location, size, amenities, and more

### 👥 User Roles & Workflows
- **Buyers**: Browse, search, save favorites, contact agents
- **Sellers**: Create listings, track performance, manage properties
- **Agents**: Client management, listing pipeline, analytics
- **Admins**: Platform oversight, user verification, content moderation

### 🔧 Platform Features
- **Newsletter Subscription**: Stay updated with market trends
- **Off-market Listings**: Exclusive property opportunities
- **Property Management Services**: Rent collection, maintenance coordination
- **Mortgage Calculator**: Affordability assessment tools
- **Tour Scheduling**: Easy viewing arrangements

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Node.js 16+ (for frontend)

### Backend Setups

```bash
# Clone repository
git clone https://github.com/Bobybuu/HousePark.git
cd HousePark/server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Environment configuration
cp .env.example .env
# Edit .env with your database and Mapbox settings

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Frontend Setup (Coming Soon)
```bash
cd ../client
npm install
npm start
```

## 🏗️ Project Structure

```
housepark/
├── server/                 # Django Backend
│   ├── config/            # Project settings
│   ├── users/             # Authentication & user management
│   ├── properties/        # Property listings & search
│   ├── inquiries/         # Contact forms & messaging
│   └── management/        # Property management services
├── client/                # React Frontend (Future)
└── docs/                  # Documentation
```

## 🔐 Authentication & Security

- **JWT + Session Authentication**: Secure API access with admin session support
- **Role-based Access Control**: Buyer, Seller, Agent, Admin permissions
- **CSRF Protection**: Built-in Django security
- **CORS Configuration**: Secure frontend-backend communication

## 🗃️ Database Schema

### Core Models
- **User**: Multi-role authentication system
- **Property**: Land, commercial, rental, apartment listings
- **PropertyImage**: Gallery management
- **Inquiry**: Buyer-seller communication
- **Feature**: Property amenities and characteristics

## 🌐 API Endpoints

### Authentication
```
POST /api/auth/register/     # User registration
POST /api/auth/login/        # User login
POST /api/auth/logout/       # User logout
GET  /api/auth/profile/      # User profile
```

### Properties
```
GET    /api/properties/      # Search & filter properties
POST   /api/properties/      # Create new listing (agents/sellers)
GET    /api/properties/:id/  # Property details
PUT    /api/properties/:id/  # Update listing
```

### User Management
```
GET    /api/users/dashboard/ # Role-specific dashboard
POST   /api/users/favorites/ # Manage saved properties
GET    /api/users/listings/  # User's property listings
```

## 🎨 Admin Features

- **Modern Dashboard**: Jazzmin-powered admin interface
- **User Management**: Role assignment and verification
- **Listing Moderation**: Approve/reject property listings
- **Analytics**: Platform performance metrics
- **Bulk Actions**: Efficient content management

## 📊 User Journeys

### 🏠 Property Buyer
1. Browse featured listings on homepage
2. Use advanced search with Mapbox integration
3. Save favorite properties
4. Contact agents through secure forms
5. Schedule property tours

### 🏢 Property Seller
1. Register and get admin approval
2. Access seller dashboard
3. Create detailed property listings
4. Upload high-quality images
5. Track listing performance and inquiries

### 👨‍💼 Real Estate Agent
1. Verified agent registration
2. Manage multiple property listings
3. Client relationship management
4. Performance analytics dashboard
5. Commission tracking

## 🔧 Configuration

### Environment Variables
```env
# Database
DB_NAME=housepark_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Mapbox
MAPBOX_ACCESS_TOKEN=your_mapbox_token

# Django
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Third-party Integrations
- **Mapbox GL JS**: Interactive property maps
- **PostgreSQL**: Robust database system
- **Jazzmin**: Modern admin interface
- **Pillow**: Image processing

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure production database
- [ ] Set up static files serving
- [ ] Configure email backend
- [ ] Set up SSL certificate
- [ ] Configure domain in ALLOWED_HOSTS

### Docker Support
```yaml
# docker-compose.yml example
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: housepark_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
  
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🛣️ Roadmap

### Phase 1: Core Platform ✅
- [x] User authentication & roles
- [x] Property listing system
- [x] Basic search functionality
- [x] Admin dashboard

### Phase 2: Enhanced Features 🚧
- [ ] Advanced Mapbox integration
- [ ] Newsletter system
- [ ] Off-market listings
- [ ] Property management services
- [ ] Mortgage calculator

### Phase 3: Advanced Capabilities 📅
- [ ] Mobile app
- [ ] AI-powered recommendations
- [ ] Virtual tours
- [ ] Payment integration
- [ ] Multi-language support

## 📞 Support

- **Documentation**: [GitHub Wiki](https://github.com/Bobybuu/HousePark/wiki)
- **Issues**: [GitHub Issues](https://github.com/Bobybuu/HousePark/issues)
- **Email**: c43057772@gmail.com

## 🙏 Acknowledgments

- Django REST Framework team
- Mapbox for excellent mapping services
- Jazzmin for the beautiful admin interface
- PostgreSQL community for robust database solutions

---

**Built  by Chrispin Odiwuor**

*Transforming real estate experiences through technology* 🏠✨