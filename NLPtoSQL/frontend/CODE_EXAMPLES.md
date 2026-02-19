# Code Examples & Best Practices

## Component Structure

### Basic Component Template
```jsx
"use client";

import { useState, useEffect } from "react";

export default function MyComponent({ prop1, prop2, onAction }) {
  const [state, setState] = useState(null);

  useEffect(() => {
    // Side effects here
  }, []);

  const handleAction = () => {
    // Logic here
  };

  return (
    <div className="space-y-4">
      {/* JSX here */}
    </div>
  );
}
```

### With Custom Hook
```jsx
"use client";

import { useApi } from "../hooks/useApi";

export default function MyComponent() {
  const { query, loading, error } = useApi();

  const handleSubmit = async (data) => {
    try {
      const result = await query(data);
      // Handle result
    } catch (err) {
      // Handle error
    }
  };

  return (
    <div>
      {loading && <Spinner />}
      {error && <ErrorMessage error={error} />}
      {/* Content */}
    </div>
  );
}
```

## Styling Patterns

### Responsive Classes
```jsx
// Mobile first, then scale up
<div className="w-full sm:w-1/2 md:w-1/3 lg:w-1/4">
  Content
</div>

// Responsive padding
<div className="p-4 sm:p-6 lg:p-8">
  Content
</div>

// Responsive grid
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
  {items.map(item => <Card key={item.id} {...item} />)}
</div>
```

### Dark Mode
```jsx
// Light mode default, dark mode with dark: prefix
<div className="bg-white text-gray-900 dark:bg-gray-950 dark:text-white">
  Content
</div>

// Conditional styling
<button className="bg-blue-600 hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-800">
  Click me
</button>
```

### Hover & Interactive States
```jsx
// Button with all states
<button className="
  rounded-lg px-4 py-2 font-medium
  bg-blue-600 text-white
  hover:bg-blue-700
  active:scale-95
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-all duration-150
">
  Click me
</button>

// Card with hover effect
<div className="
  rounded-lg border border-gray-200
  bg-white p-4
  hover:shadow-md hover:shadow-blue-200
  transition-all duration-200
  dark:border-gray-700 dark:bg-gray-900
">
  Content
</div>
```

## API Integration

### Using useApi Hook
```jsx
import { useApi } from "../hooks/useApi";

export default function QueryForm() {
  const { query, loading, error } = useApi();
  const [input, setInput] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await query(input);
      console.log("Success:", response);
    } catch (err) {
      console.error("Error:", err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        disabled={loading}
      />
      <button type="submit" disabled={loading || !input.trim()}>
        {loading ? "Loading..." : "Submit"}
      </button>
      {error && <p className="text-red-600">{error}</p>}
    </form>
  );
}
```

### Error Handling
```jsx
const handleApiCall = async () => {
  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    console.error("API Error:", err.message);
    setError(err.message);
    throw err;
  }
};
```

## State Management

### Local Component State
```jsx
const [messages, setMessages] = useState([]);

// Add message
setMessages(prev => [...prev, newMessage]);

// Update message
setMessages(prev => 
  prev.map(msg => msg.id === id ? { ...msg, ...updates } : msg)
);

// Remove message
setMessages(prev => prev.filter(msg => msg.id !== id));
```

### Multiple Related States
```jsx
const [state, setState] = useState({
  loading: false,
  error: null,
  data: null,
});

// Update
setState(prev => ({
  ...prev,
  loading: true,
}));
```

## Common Patterns

### Loading Spinner
```jsx
import { Loader } from "lucide-react";

{loading && (
  <div className="flex items-center justify-center">
    <Loader className="animate-spin text-blue-600" size={32} />
  </div>
)}
```

### Error Message
```jsx
{error && (
  <div className="rounded-lg border border-red-200 bg-red-50 p-4 dark:border-red-900 dark:bg-red-950">
    <p className="text-sm font-medium text-red-800 dark:text-red-200">
      Error: {error}
    </p>
  </div>
)}
```

### Empty State
```jsx
{items.length === 0 ? (
  <div className="flex h-full items-center justify-center text-center">
    <div>
      <p className="text-lg font-semibold text-gray-900 dark:text-white">
        No items found
      </p>
      <p className="mt-2 text-sm text-gray-600 dark:text-gray-400">
        Try adjusting your search
      </p>
    </div>
  </div>
) : (
  // Content
)}
```

### Conditional Rendering
```jsx
// Simple condition
{isVisible && <Component />}

// Ternary
{isLoading ? <Spinner /> : <Content />}

// Multiple conditions
{isLoading && <Spinner />}
{error && <Error />}
{!isLoading && !error && data && <Content data={data} />}
```

## Form Handling

### Controlled Input
```jsx
const [input, setInput] = useState("");

<input
  type="text"
  value={input}
  onChange={(e) => setInput(e.target.value)}
  placeholder="Enter text..."
  className="rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none"
/>
```

### Form Submission
```jsx
const handleSubmit = async (e) => {
  e.preventDefault();
  
  if (!input.trim()) return;
  
  setLoading(true);
  try {
    const result = await api.submit(input);
    setInput("");
    // Handle success
  } catch (err) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
};

<form onSubmit={handleSubmit} className="flex gap-2">
  <input
    value={input}
    onChange={(e) => setInput(e.target.value)}
    disabled={loading}
  />
  <button type="submit" disabled={loading || !input.trim()}>
    Submit
  </button>
</form>
```

## Performance Optimization

### Memoization
```jsx
import { useMemo, useCallback } from "react";

// Memoize expensive computation
const sortedData = useMemo(() => {
  return data.sort((a, b) => a.name.localeCompare(b.name));
}, [data]);

// Memoize callback
const handleClick = useCallback(() => {
  // Logic
}, [dependency]);
```

### Lazy Loading
```jsx
import dynamic from "next/dynamic";

const HeavyComponent = dynamic(() => import("./HeavyComponent"), {
  loading: () => <Spinner />,
});

export default function Page() {
  return <HeavyComponent />;
}
```

## Testing Patterns

### Component Testing
```jsx
import { render, screen, fireEvent } from "@testing-library/react";
import MyComponent from "./MyComponent";

describe("MyComponent", () => {
  it("renders correctly", () => {
    render(<MyComponent />);
    expect(screen.getByText("Expected Text")).toBeInTheDocument();
  });

  it("handles click", () => {
    render(<MyComponent />);
    fireEvent.click(screen.getByRole("button"));
    expect(screen.getByText("Updated Text")).toBeInTheDocument();
  });
});
```

## Accessibility Best Practices

### Semantic HTML
```jsx
// Good
<button onClick={handleClick}>Click me</button>
<form onSubmit={handleSubmit}>
  <label htmlFor="email">Email</label>
  <input id="email" type="email" />
</form>

// Avoid
<div onClick={handleClick}>Click me</div>
<div>
  <span>Email</span>
  <input type="text" />
</div>
```

### ARIA Labels
```jsx
// Icon button needs label
<button
  onClick={toggleTheme}
  aria-label="Toggle theme"
  className="p-2"
>
  <Moon size={20} />
</button>

// Form input needs label
<label htmlFor="search">Search</label>
<input id="search" type="text" />
```

### Keyboard Navigation
```jsx
// Handle Enter key
<input
  onKeyDown={(e) => {
    if (e.key === "Enter") {
      handleSubmit();
    }
  }}
/>

// Tab order
<div>
  <button tabIndex={0}>First</button>
  <button tabIndex={1}>Second</button>
</div>
```

## Common Mistakes to Avoid

### ❌ Don't
```jsx
// Inline object in render (creates new object each render)
<Component style={{ color: "red" }} />

// Missing key in list
{items.map(item => <Item item={item} />)}

// State mutation
state.push(newItem);

// Missing dependency in useEffect
useEffect(() => {
  // Uses 'data' but not in dependency array
}, []);

// Conditional hooks
if (condition) {
  const value = useState(null);
}
```

### ✅ Do
```jsx
// Define object outside render
const style = { color: "red" };
<Component style={style} />

// Always use key
{items.map(item => <Item key={item.id} item={item} />)}

// Create new array
setState([...state, newItem]);

// Include dependencies
useEffect(() => {
  // Uses 'data'
}, [data]);

// Hooks at top level
const [value, setValue] = useState(null);
if (condition) {
  // Use value
}
```

## Debugging Tips

### Console Logging
```jsx
// Log component render
console.log("Component rendered", { prop1, prop2 });

// Log state changes
useEffect(() => {
  console.log("State updated:", state);
}, [state]);

// Log API calls
console.log("API Call:", { url, method, body });
```

### React DevTools
- Install React DevTools browser extension
- Inspect component props and state
- Track component renders
- Profile performance

### Network Tab
- Check API requests/responses
- Verify request headers
- Check response status codes
- Monitor network timing

---

**Remember**: Write code for humans first, machines second. Keep it simple, readable, and maintainable.
