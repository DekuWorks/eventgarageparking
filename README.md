# Event Garage Parking - Django Backend

> **A web platform connecting homeowners with parking spaces to event attendees seeking convenient, affordable parking near venues**

## 🚗 What We're Building

**Event Garage Parking** (https://eventgarageparking.com/) is a peer-to-peer parking marketplace that solves a real problem: expensive, crowded parking at events.

### The Problem
- Event parking is expensive ($30-50+ per spot)
- Parking lots are often far from venues
- Last-minute parking searches are stressful
- Homeowners near venues have unused driveways and garages

### Our Solution
A web platform where:
- **Homeowners** list their driveways, garages, and parking spaces near event venues
- **Event attendees** book affordable, convenient parking spots in residential areas
- **Everyone wins**: Homeowners earn extra income, customers save money and walk less

### Platform Features

#### For Customers (Event Attendees)
- 🔍 **Search & Discover**: Find parking spots near your event by address or venue
- 📅 **Instant Booking**: Reserve your spot with date/time selection
- 💳 **Secure Payment**: Pay safely through the platform (Stripe integration)
- 📍 **GPS Navigation**: Get directions to your reserved spot
- ⭐ **Reviews & Ratings**: See verified reviews from other customers
- 📧 **Email Confirmations**: Receive booking details and access instructions

#### For Hosts (Homeowners)
- 🏠 **List Your Space**: Post your driveway, garage, or parking spot
- 💰 **Set Your Price**: Choose your hourly/daily rates
- 📆 **Manage Availability**: Control when your space is available
- 💵 **Instant Payouts**: Get paid directly to your bank account
- ⭐ **Build Reputation**: Earn ratings from satisfied customers
- 📊 **Track Earnings**: View analytics and booking history

#### Platform Security & Trust
- ✅ **Verified Hosts**: Host identity and address verification
- ✅ **Verified Customers**: Email and phone verification
- 🔒 **Secure Payments**: PCI-compliant payment processing
- 🛡️ **Insurance Ready**: Framework for parking insurance integration
- 📱 **Real-time Support**: Customer service and dispute resolution

## 💼 Business Model

### Revenue Streams
1. **Service Fee**: Platform takes a percentage (e.g., 15-20%) of each booking
2. **Host Premium Features**: Featured listings, analytics, priority support
3. **Customer Premium**: Subscription for frequent parkers with discounts

### User Types

#### 1. **Customers** (Event Attendees)
People looking for parking near events (concerts, sports games, festivals, etc.)
- Search for available parking spots
- Book and pay for reservations
- Rate and review parking spots
- Manage their bookings

#### 2. **Hosts** (Homeowners/Property Owners)
People with parking spaces (driveways, garages, empty lots) near event venues
- List their parking spaces
- Set prices and availability
- Receive bookings and payments
- Earn passive income
- Build host reputation

#### 3. **Drivers** (Valet Service - Future)
Professional drivers who can move cars for customers
- Offer valet parking services
- Pick up and park customer vehicles
- Premium service tier

#### 4. **Admins** (Platform Operators)
Internal team managing the platform
- Verify hosts and listings
- Handle disputes
- Manage platform settings
- View analytics and reports

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

## 🔌 API Endpoints (To Be Implemented)

### Authentication
- `POST /api/auth/register/` - User registration (email/password)
- `POST /api/auth/login/` - User login
- `POST /api/auth/social/google/` - Google OAuth
- `POST /api/auth/social/apple/` - Apple Sign In
- `POST /api/auth/social/facebook/` - Facebook Login
- `POST /api/auth/logout/` - User logout
- `POST /api/auth/refresh/` - Refresh JWT token
- `POST /api/auth/verify-email/` - Email verification
- `POST /api/auth/verify-phone/` - Phone verification

### User Profile
- `GET /api/users/me/` - Get current user profile
- `PUT /api/users/me/` - Update user profile
- `POST /api/users/me/upload-photo/` - Upload profile picture
- `GET /api/users/{id}/` - Get public user profile (for reviews)

### Parking Spots (Listings)
- `GET /api/spots/` - Search/filter available parking spots
- `GET /api/spots/near/` - Find spots near address/coordinates
- `GET /api/spots/{id}/` - Get spot details
- `POST /api/spots/` - Create new listing (hosts only)
- `PUT /api/spots/{id}/` - Update listing
- `DELETE /api/spots/{id}/` - Delete listing
- `POST /api/spots/{id}/photos/` - Upload spot photos
- `GET /api/spots/{id}/availability/` - Check availability calendar
- `PUT /api/spots/{id}/availability/` - Update availability

### Bookings (Reservations)
- `GET /api/bookings/` - List user's bookings
- `GET /api/bookings/{id}/` - Get booking details
- `POST /api/bookings/` - Create new booking
- `PUT /api/bookings/{id}/cancel/` - Cancel booking
- `GET /api/bookings/host/` - List bookings for host's spots

### Payments
- `POST /api/payments/setup-intent/` - Setup payment method
- `POST /api/payments/process/` - Process booking payment
- `GET /api/payments/methods/` - List saved payment methods
- `DELETE /api/payments/methods/{id}/` - Remove payment method
- `POST /api/payouts/setup/` - Setup host payout account (Stripe Connect)
- `GET /api/payouts/balance/` - Get host earnings balance
- `POST /api/payouts/transfer/` - Request payout

### Reviews & Ratings
- `GET /api/reviews/spot/{spot_id}/` - Get reviews for a spot
- `POST /api/reviews/` - Submit a review
- `GET /api/reviews/user/{user_id}/` - Get reviews for a user
- `PUT /api/reviews/{id}/` - Edit review
- `DELETE /api/reviews/{id}/` - Delete review

### Search & Discovery
- `GET /api/search/` - Advanced search with filters
- `GET /api/search/venues/` - Search popular venues
- `GET /api/search/events/` - Search upcoming events near location

### Favorites (Wishlist)
- `GET /api/favorites/` - List saved spots
- `POST /api/favorites/{spot_id}/` - Add spot to favorites
- `DELETE /api/favorites/{spot_id}/` - Remove from favorites

### Notifications
- `GET /api/notifications/` - List user notifications
- `PUT /api/notifications/{id}/read/` - Mark as read
- `PUT /api/notifications/read-all/` - Mark all as read

## 🎯 Development Roadmap

### Phase 1: Core Models (Current)
- [x] UserProfile model with authentication
- [ ] **ParkingSpot model**:
  - Location (address, coordinates, geocoding)
  - Spot details (type, size, features)
  - Pricing (hourly, daily rates)
  - Availability calendar
  - Photos (multiple images)
  - Host relationship
- [ ] **Booking model**:
  - Customer & parking spot relationship
  - Reservation dates/times
  - Booking status (pending, confirmed, completed, cancelled)
  - Total price calculation
  - Access instructions
- [ ] **Payment model**:
  - Stripe payment integration
  - Transaction tracking
  - Payout scheduling for hosts
  - Refund handling
- [ ] **Review model**:
  - Customer reviews for spots
  - Host reviews for customers
  - Rating system (1-5 stars)
  - Review moderation

### Phase 2: REST API
- [ ] Install Django REST Framework + JWT authentication
- [ ] Authentication endpoints (register, login, social auth)
- [ ] Parking spot endpoints (search, list, create, update)
- [ ] Booking endpoints (create booking, manage reservations)
- [ ] Payment endpoints (process payment, payouts)
- [ ] Review endpoints (submit review, view ratings)
- [ ] User profile endpoints (view/edit profile)

### Phase 3: Search & Discovery
- [ ] Geospatial search (find spots near location/venue)
- [ ] Availability filtering (date/time search)
- [ ] Price filtering and sorting
- [ ] Map view integration (Google Maps API)
- [ ] Distance calculation from venues
- [ ] Popular venue database

### Phase 4: Payments & Payouts
- [ ] Stripe Connect integration for hosts
- [ ] Payment method management
- [ ] Automatic payouts to hosts
- [ ] Transaction fee calculation
- [ ] Refund processing
- [ ] Earnings dashboard for hosts

### Phase 5: Notifications & Communication
- [ ] Email notifications (booking confirmations, reminders)
- [ ] SMS notifications (access codes, updates)
- [ ] Push notifications (mobile app ready)
- [ ] In-app messaging between hosts and customers
- [ ] Calendar sync integration

### Phase 6: Advanced Features
- [ ] Real-time availability updates
- [ ] Recurring bookings (season passes)
- [ ] Group bookings (multiple spots)
- [ ] Dynamic pricing (surge pricing for high-demand events)
- [ ] Insurance integration
- [ ] Dispute resolution system
- [ ] Analytics dashboard
- [ ] Mobile apps (iOS/Android)

### Phase 7: Testing & Deployment
- [ ] Unit tests for all models
- [ ] API endpoint tests
- [ ] Integration tests
- [ ] Performance testing
- [ ] Security audit
- [ ] CI/CD pipeline setup
- [ ] Production deployment (AWS/Heroku)
- [ ] Domain setup and SSL

## Contributing

This is a clean, organized Django project structure following best practices. All apps live in the `src/` directory for better organization and maintainability.

## License

Private - Event Garage Parking LLC
