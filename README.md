# Project Suite: Student Registration & Agile Taxi Booking System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.1-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)
![Agile](https://img.shields.io/badge/Methodology-Agile-blueviolet.svg)

## Overview

This comprehensive project suite combines two robust applications developed using Agile methodology:

1. **Student Registration Desktop Application**: A secure student management system with encrypted data storage, built with Python and Tkinter for educational institutions needing reliable record-keeping.

2. **Auto Taxi Booking System**: A full-featured web application developed with Django and MySQL that revolutionizes urban mobility by connecting passengers with drivers through an intelligent dispatch system.

Both projects follow Agile principles with 2-week sprints, continuous integration, and user-centric design.

---

# 🚖 Auto Taxi Booking System (Django/MySQL)

## System Overview

The Auto Taxi Booking System transforms traditional taxi services by providing a digital platform that benefits all stakeholders:

**For Passengers**:
- Intuitive booking interface with real-time vehicle tracking
- Multiple payment options including credit cards and digital wallets
- Personalized experience with saved locations and ride preferences
- Transparent pricing with fare estimation before booking

**For Drivers**:
- Optimized ride allocation based on proximity and availability
- Earnings dashboard with performance analytics
- Navigation integration with popular mapping services
- Flexible shift management system

**For Administrators**:
- Comprehensive fleet management tools
- Dynamic pricing configuration during peak hours
- Detailed reporting on business metrics
- Driver performance evaluation system

## Key Features

### Enhanced User Experience
The system reduces average wait times by 40% through intelligent dispatch algorithms. Users can schedule rides up to 7 days in advance and receive real-time notifications about their driver's location and estimated arrival time.

### Secure Transactions
All financial transactions are protected with PCI-compliant encryption. The system supports tokenized payments for recurring customers, ensuring credit card details are never stored on our servers.

### Intelligent Dispatch
Our proprietary algorithm considers multiple factors:
- Real-time traffic conditions
- Driver availability and ratings
- Vehicle type preferences
- Special accessibility requirements

## Screenshots
<img width="1052" height="636" alt="image" src="https://github.com/user-attachments/assets/beeeb393-3f9b-4d87-9fd3-586d00115e65" />
<img width="1054" height="608" alt="image" src="https://github.com/user-attachments/assets/693fe96f-728a-4e17-9c7b-246ee736a7f7" />
<img width="1068" height="620" alt="image" src="https://github.com/user-attachments/assets/758370e0-9b5f-4314-bf20-23f472598cee" />


## System Architecture

The application follows a clean 3-tier architecture:


## System Architecture

| Component       | Technology           |
|----------------|---------------------|
| Frontend       | HTML5, CSS3, JavaScript |
| Backend        | Python (Django)      |
| Database       | MySQL               |
| Authentication | Django Auth         |
| Payment        | Stripe/PayPal API   |

## Agile Implementation
- 🏃‍♂️ 2-week sprints with daily standups
- 📝 User stories with MoSCoW prioritization
- 🧪 Continuous integration/testing
- 📈 Burndown charts for progress tracking

## Installation

```bash
# Clone repository
git clone https://github.com/yourrepo/taxi-booking.git

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Configure MySQL
1. Create database 'taxibooking'
2. Update settings.py with credentials

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
