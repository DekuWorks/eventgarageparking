# Event Garage Parking - Django Backend

A clean, organized Django backend for the **Event Garage Parking** platform - a peer-to-peer parking marketplace connecting homeowners with parking spots to customers looking for convenient event parking.

## About Event Garage Parking

Event Garage Parking (https://eventgarageparking.com/) enables homeowners to rent out their driveways and parking spaces to people attending events. The platform features:

- **Verified Hosts**: Homeowners offering residential parking spaces
- **Instant Booking**: Quick and easy reservation system
- **Secure Payments**: Integrated payment processing via Stripe
- **Multiple User Types**: Customers (seeking parking), Drivers, and Valets

## Project Structure

```
eventgarageparking/
├── config/              # Django project configuration
│   ├── settings.py     # Main settings file
│   ├── urls.py         # Root URL configuration
│   ├── wsgi.py         # WSGI application
│   └── asgi.py         # ASGI application
├── src/                 # All Django apps organized in one place
│   ├── accounts/        # User authentication & profiles
│   │   └── models.py    # UserProfile (custom user model)
│   ├── customers/       # Customer management
│   ├── drivers/         # Driver management
│   ├── transactions/    # Booking & payment transactions
│   ├── analytics/       # Platform analytics & reporting
│   └── Settings/        # User settings & preferences
├── venv/               # Virtual environment (not in git)
├── manage.py
├── requirements.txt
└── README.md
```

## Key Features

### UserProfile Model
The custom user model includes:
- **Authentication**: Email-based login with social auth (Google, Apple, Facebook)
- **User Types**: Customer, Driver, or Valet
- **Location Tracking**: Address geocoding and real-time GPS coordinates
- **Payment Integration**: Multiple payment methods and payout preferences
- **Ratings**: 1-5 star rating system
- **Verification**: Email, phone, and identity verification
- **Profile**: Bio, profile image (S3), emergency contacts

## Setup Instructions

### 1. Activate Virtual Environment
```bash
cd ~/egp/projects/eventgarageparking
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create Superuser
```bash
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000/admin

## Development

### Creating New Apps
All apps should be created in the `src/` directory:
```bash
cd src
django-admin startapp your_app_name
```

Then add the app to `INSTALLED_APPS` in `config/settings.py`.

### Making Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

## Technology Stack

- **Django**: 6.0.1
- **Python**: 3.13.7
- **Database**: SQLite (development) / PostgreSQL (production)
- **Image Processing**: Pillow 12.1.0
- **Payment Processing**: Stripe (planned integration)

## Environment Variables (Production)

Create a `.env` file with:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgres://...
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
STRIPE_SECRET_KEY=your-stripe-key
```

## API Endpoints (To Be Implemented)

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/social/` - Social authentication

### Bookings
- `GET /api/bookings/` - List user bookings
- `POST /api/bookings/` - Create new booking
- `GET /api/bookings/{id}/` - Booking details

### Parking Spots
- `GET /api/spots/` - Search available spots
- `POST /api/spots/` - List a parking spot (hosts)
- `GET /api/spots/{id}/` - Spot details

## Next Steps

1. **Implement Business Logic Models**:
   - ParkingSpot model (location, availability, pricing)
   - Booking model (reservations, status tracking)
   - Payment model (Stripe integration)
   - Review model (ratings and feedback)

2. **Build REST API**:
   - Install Django REST Framework
   - Create serializers and viewsets
   - Implement authentication (JWT)

3. **Add Core Features**:
   - Real-time location tracking
   - Push notifications
   - Payment processing
   - Booking management
   - Search & filters

4. **Testing & Deployment**:
   - Write comprehensive tests
   - Set up CI/CD pipeline
   - Deploy to production (AWS/Heroku)

## Contributing

This is a clean, organized Django project structure following best practices. All apps live in the `src/` directory for better organization and maintainability.

## License

Private - Event Garage Parking LLC
