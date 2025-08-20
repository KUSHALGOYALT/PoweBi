# Hexa BI Visualizer

A Django-based authentication system with integrated PowerBI dashboard for secure business intelligence visualization.

## Features

- 🔐 **Secure Authentication**: Django-based login system
- 📊 **PowerBI Integration**: Seamless iframe embedding of PowerBI reports
- 🎨 **Professional Design**: Clean black and white theme with Hexa Climate branding
- 📱 **Responsive Layout**: Optimized for desktop and mobile viewing
- 🚀 **Production Ready**: PostgreSQL support with SQLite fallback

## Quick Start

### Prerequisites

- Python 3.8+
- Django 4.2.7
- Optional: PostgreSQL (falls back to SQLite)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hexa-Climate/hexa-bi-visualizer.git
   cd hexa-bi-visualizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   USE_SQLITE=1 python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   USE_SQLITE=1 python manage.py createsuperuser
   ```

5. **Start the server**
   ```bash
   USE_SQLITE=1 python manage.py runserver 127.0.0.1:8002
   ```

6. **Access the application**
   - URL: http://127.0.0.1:8002/
   - Default admin credentials: admin / admin123

## Configuration

### Database

- **SQLite** (default): Set `USE_SQLITE=1` environment variable
- **PostgreSQL**: Configure database settings in `authdemo/settings.py`

### PowerBI Integration

The dashboard includes an embedded PowerBI report. To customize:

1. Update the iframe URL in `templates/dashboard.html`
2. Replace with your PowerBI report embed URL

## Project Structure

```
hexa-bi-visualizer/
├── accounts/                 # Authentication app
│   ├── views.py             # Login/logout logic
│   ├── urls.py              # URL patterns
│   └── ...
├── authdemo/                # Django project settings
│   ├── settings.py          # Configuration
│   ├── urls.py              # Main URL routing
│   └── ...
├── static/                  # Static files
│   ├── css/style.css        # Styling
│   └── js/auth.js           # JavaScript
├── templates/               # HTML templates
│   ├── login.html           # Login page
│   └── dashboard.html       # Dashboard page
├── requirements.txt         # Python dependencies
└── manage.py               # Django management
```

## Features Overview

### Authentication System
- Secure Django authentication
- Session management
- Login/logout functionality
- User account management

### Dashboard
- Professional black header with Hexa Climate logo
- Welcome message with username
- Logout functionality
- Full-screen PowerBI report display

### Design
- Clean black and white theme
- Hexa Climate branding
- Responsive design for all devices
- Professional business appearance

## Development

### Adding New Features

1. **Models**: Add to `accounts/models.py`
2. **Views**: Update `accounts/views.py`
3. **Templates**: Modify files in `templates/`
4. **Styling**: Edit `static/css/style.css`

### Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files

```bash
python manage.py collectstatic
```

## Production Deployment

### PostgreSQL Setup

1. Install PostgreSQL
2. Create database and user
3. Update `authdemo/settings.py` with database credentials
4. Remove `USE_SQLITE=1` from commands

### Security

- Change `SECRET_KEY` in settings.py
- Set `DEBUG = False` for production
- Configure `ALLOWED_HOSTS`
- Use environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit a pull request

## License

This project is developed for Hexa Climate internal use.

## Support

For support and questions, contact the Hexa Climate development team.

---

**Hexa Climate** - Advanced Climate Intelligence Solutions
