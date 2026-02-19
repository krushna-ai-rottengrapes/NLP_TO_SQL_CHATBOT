# Authentication Usage Examples

## Import AuthContext

```javascript
import { useAuth } from "@/app/contexts/AuthContext";
```

## Access User Data

```javascript
function ProfileComponent() {
  const { user, client } = useAuth();

  return (
    <div>
      <h1>Welcome, {user?.full_name}</h1>
      <p>Email: {user?.username}</p>
      <p>Role: {user?.role}</p>
      <p>Company: {client?.client_name}</p>
    </div>
  );
}
```

## Check User Role

```javascript
function AdminPanel() {
  const { user, isOwner, isViewer } = useAuth();

  if (isOwner()) {
    return <div>Admin Controls</div>;
  }

  if (isViewer()) {
    return <div>Read-only View</div>;
  }

  return null;
}
```

## Conditional Rendering

```javascript
function Dashboard() {
  const { user, isOwner } = useAuth();

  return (
    <div>
      <h1>Dashboard</h1>
      
      {/* Show button only for owners */}
      {isOwner() && (
        <button>Create New Dashboard</button>
      )}

      {/* Access user properties */}
      <p>User ID: {user?.id}</p>
      <p>Client ID: {user?.client_id}</p>
    </div>
  );
}
```

## Logout

```javascript
function Header() {
  const { user, logout } = useAuth();
  const router = useRouter();

  const handleLogout = async () => {
    await logout();
    router.push('/login');
  };

  return (
    <header>
      <span>{user?.full_name}</span>
      <button onClick={handleLogout}>Logout</button>
    </header>
  );
}
```

## Loading State

```javascript
function ProtectedPage() {
  const { user, loading } = useAuth();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!user) {
    return <div>Please login</div>;
  }

  return <div>Protected Content</div>;
}
```

## User Object Structure

```javascript
user = {
  id: 1,
  username: "pm@rg.tech",
  role: "internal_superuser",  // or "viewer"
  full_name: "Admin User",
  mobile_number: "1234567890",
  client_id: 1,
  created_at: "2025-12-03T17:17:26.194730+05:30",
  updated_at: null
}
```

## Client Object Structure

```javascript
client = {
  id: 1,
  client_name: "Rotten Grapes",
  email: "office@rottengrapes.tech",
  mobile_number: "99999999",
  company_name: null,
  company_email: null,
  plan_id: null
}
```

## Role-Based Access Control

```javascript
function FeatureComponent() {
  const { user } = useAuth();

  const canEdit = user?.role === "internal_superuser";
  const canView = user?.role === "viewer" || user?.role === "internal_superuser";

  return (
    <div>
      {canView && <ViewPanel />}
      {canEdit && <EditPanel />}
    </div>
  );
}
```

## API Calls with Authentication

```javascript
import api from "@/lib/api";

function DataComponent() {
  const { user } = useAuth();
  const [data, setData] = useState(null);

  useEffect(() => {
    // Token automatically added by axios interceptor
    api.get('/some-endpoint')
      .then(res => setData(res.data))
      .catch(err => console.error(err));
  }, []);

  return <div>{/* Render data */}</div>;
}
```
