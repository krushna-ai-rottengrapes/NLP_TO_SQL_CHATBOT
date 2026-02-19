# Authentication Flow Documentation

## Overview
Enterprise-grade authentication using HTTP-only cookies with JWT tokens and in-memory caching.

## Architecture

### 1. Login Flow
```
User Login → /api/auth/login → Backend API → HTTP-only Cookie Set → User Data in SessionStorage
```

**Steps:**
1. User submits credentials via `/login` page
2. Frontend calls `/api/auth/login` (Next.js API route)
3. API route forwards request to `http://127.0.0.1:8000/users/login`
4. Backend returns JWT token + user data
5. API route sets HTTP-only cookie with token
6. User data stored in sessionStorage (not token)
7. User redirected to `/dashboard`

### 2. Token Management

**Storage Strategy:**
- **Token**: HTTP-only cookie (secure, not accessible via JavaScript)
- **User Data**: sessionStorage (accessible, cleared on tab close)
- **Token Cache**: In-memory cache (performance optimization)

**Token Caching:**
```javascript
First API Call → Fetch token from /api/auth/me → Cache in memory
Subsequent Calls → Use cached token (no extra requests)
Login/Logout → Clear cache
401 Error → Clear cache + redirect to login
```

### 3. API Calls Flow
```
Component → axios.get() → Interceptor → Get Cached Token → Add Bearer Header → Backend API
```

**Token Retrieval:**
1. Interceptor checks in-memory cache
2. If not cached, calls `/api/auth/me` once
3. `/api/auth/me` reads HTTP-only cookie
4. Token cached for subsequent requests
5. Token added to Authorization header

### 4. Route Protection

**Middleware (`src/middleware.js`):**
- Reads HTTP-only cookie
- Redirects unauthenticated users to `/login`
- Redirects authenticated users away from `/login`
- Injects token into request headers for SSR

### 5. User State Management

**AuthContext (`src/app/contexts/AuthContext.js`):**
```javascript
const { user, login, logout, isOwner, isViewer } = useAuth();

// User object structure:
{
  id: 1,
  username: "pm@rg.tech",
  role: "internal_superuser",
  full_name: "Admin User",
  client_id: 1
}
```

**Usage Examples:**
```javascript
// Check user role
const { user, isOwner } = useAuth();
if (isOwner()) {
  // Show admin features
}

// Access user data
console.log(user.full_name);
console.log(user.role);
```

### 6. Logout Flow
```
User Logout → /api/auth/logout → Clear HTTP-only Cookie → Clear SessionStorage → Clear Cache → Redirect to /login
```

## Security Features

1. **HTTP-only Cookies**: Token not accessible via JavaScript (XSS protection)
2. **SameSite Strict**: CSRF protection
3. **SessionStorage**: User data cleared on tab close
4. **Token Caching**: Reduces API calls, improves performance
5. **Middleware Protection**: Server-side route guarding
6. **401 Auto-logout**: Automatic session cleanup

## API Endpoints

### Frontend API Routes
- `POST /api/auth/login` - Login and set cookie
- `POST /api/auth/logout` - Clear cookie
- `GET /api/auth/me` - Get token from cookie

### Backend API Routes
- `POST /users/login` - Authenticate user

## Files Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── api/auth/
│   │   │   ├── login/route.js      # Login API route
│   │   │   ├── logout/route.js     # Logout API route
│   │   │   └── me/route.js         # Token retrieval
│   │   ├── contexts/
│   │   │   └── AuthContext.js      # User state management
│   │   └── login/page.js           # Login UI
│   ├── lib/
│   │   └── api.js                  # Axios with token caching
│   └── middleware.js               # Route protection
```

## Usage in Components

```javascript
import { useAuth } from "@/app/contexts/AuthContext";

function MyComponent() {
  const { user, isOwner, logout } = useAuth();

  return (
    <div>
      <p>Welcome, {user?.full_name}</p>
      {isOwner() && <AdminPanel />}
      <button onClick={logout}>Logout</button>
    </div>
  );
}
```

## Environment Variables

```env
# Backend API URL (default: http://127.0.0.1:8000)
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## Testing Credentials

```json
{
  "username": "pm@rg.tech",
  "password": "admin"
}
```


```
Login → Cookie (access_token)
         ↓
    Middleware (checks cookie)
         ↓
    /api/auth/me (reads cookie, calls backend)
         ↓
    Returns: { user, client, token }
         ↓
    API lib caches token for backend calls
    
``` 
