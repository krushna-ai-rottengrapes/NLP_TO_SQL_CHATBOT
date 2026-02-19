# Architecture & Design Documentation

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Browser                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Next.js App (page.js)                   │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │           Navbar Component                     │  │  │
│  │  │  [Theme Toggle] [GitHub Link]                 │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  │                                                       │  │
│  │  ┌─────────────────┬──────────────────────────────┐  │  │
│  │  │  Chat Panel     │    Result Panel              │  │  │
│  │  │                 │                              │  │  │
│  │  │ ┌─────────────┐ │ ┌──────────────────────────┐ │  │  │
│  │  │ │ Messages    │ │ │ KPI Cards / Data Table   │ │  │  │
│  │  │ │ - User Q    │ │ │ - Sorting                │ │  │  │
│  │  │ │ - SQL Query │ │ │ - Pagination             │ │  │  │
│  │  │ │ - Tables    │ │ │ - Search                 │ │  │  │
│  │  │ │ - Re-exec   │ │ │ - CSV Export             │ │  │  │
│  │  │ └─────────────┘ │ │ - FAB Button             │ │  │  │
│  │  │                 │ │                          │ │  │  │
│  │  │ ┌─────────────┐ │ └──────────────────────────┘ │  │  │
│  │  │ │ Input Form  │ │                              │  │  │
│  │  │ │ [Send Btn]  │ │                              │  │  │
│  │  │ └─────────────┘ │                              │  │  │
│  │  └─────────────────┴──────────────────────────────┘  │  │
│  │         ▲ Resizable Divider (draggable)              │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTP
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend API                              │
│  POST /database/query                                       │
│  POST /database/execute-sql                                 │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

### Query Flow
```
User Input
    │
    ▼
ChatPanel.handleSubmit()
    │
    ├─ useApi.query(question)
    │   │
    │   ▼
    │ POST /database/query
    │   │
    │   ▼
    │ Response: { sql_query, filtered_tables, ... }
    │
    ├─ setMessages([...messages, newMessage])
    │
    └─ onQueryReceived(sql_query)
        │
        ▼
    ResultPanel receives sqlQuery
        │
        ├─ useApi.executeSql(sqlQuery)
        │   │
        │   ▼
        │ POST /database/execute-sql
        │   │
        │   ▼
        │ Response: { data, columns }
        │
        ├─ isSingleValue ? KPICard : DataTable
        │
        └─ setResult(response)
```

### Re-execute Flow
```
User clicks "Re-execute Query"
    │
    ▼
ChatMessage.onReexecute(message)
    │
    ▼
ChatPanel.handleReexecute(sql_query)
    │
    ▼
onReexecute(sql_query)
    │
    ▼
ResultPanel receives new sqlQuery
    │
    ▼
useEffect triggers executeSql()
    │
    ▼
Results update
```

## Component Hierarchy

```
App (page.js)
├── Navbar
│   └── useTheme hook
├── PanelGroup (react-resizable-panels)
│   ├── Panel (Chat)
│   │   └── ChatPanel
│   │       ├── ChatMessage (multiple)
│   │       │   └── SyntaxHighlighter
│   │       └── Input Form
│   ├── PanelResizeHandle
│   └── Panel (Results)
│       └── ResultPanel
│           ├── KPICard (conditional)
│           ├── DataTable (conditional)
│           │   └── TanStack Table
│           └── FAB Button
```

## State Management

### Global State (App Level)
```javascript
const [currentSqlQuery, setCurrentSqlQuery] = useState(null);
// Shared between ChatPanel and ResultPanel
```

### Local State (Component Level)

**ChatPanel**:
- `messages`: Array of chat messages
- `input`: Current input text
- `localLoading`: Loading state

**ResultPanel**:
- `result`: API response data
- `localLoading`: Loading state
- `showFAB`: FAB visibility

**DataTable**:
- `sorting`: Sort configuration
- `globalFilter`: Search text
- `pagination`: Page state

**Navbar**:
- `theme`: Current theme
- `mounted`: Hydration flag

## Styling Strategy

### Design Tokens (CSS Variables)
```css
--background: Light/dark background
--foreground: Text color
--border: Border color
--muted: Secondary background
--accent: Primary blue
```

### Tailwind Utilities
- Responsive classes: `sm:`, `md:`, `lg:`
- Dark mode: `dark:` prefix
- Hover states: `hover:`, `dark:hover:`
- Disabled states: `disabled:`

### Component Styling
- Inline Tailwind classes (no CSS files per component)
- Consistent spacing: 4px grid
- Consistent shadows: `shadow-sm`, `shadow-md`
- Consistent rounded corners: `rounded-lg`

## Performance Optimizations

1. **Code Splitting**: Next.js automatic route splitting
2. **Image Optimization**: No images used (icons via Lucide)
3. **CSS Purging**: Tailwind removes unused styles
4. **Lazy Loading**: Components load on demand
5. **Memoization**: TanStack Table handles re-renders
6. **API Caching**: No caching (fresh data on each query)

## Accessibility

- Semantic HTML (`<button>`, `<form>`, `<table>`)
- ARIA labels on icon buttons
- Keyboard navigation support
- Color contrast meets WCAG AA
- Focus states visible
- Loading states announced

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile browsers: iOS Safari 12+, Chrome Android

## Error Handling

```
API Error
    │
    ├─ useApi sets error state
    │
    ├─ Component catches error
    │
    └─ User sees error message
        │
        └─ Can retry by submitting again
```

## Security Considerations

1. **No sensitive data in localStorage** (only theme)
2. **CORS handled by backend**
3. **No SQL injection** (backend responsibility)
4. **No XSS** (React escapes by default)
5. **No CSRF** (backend should implement)

## Deployment Checklist

- [ ] Environment variables configured
- [ ] Backend API URL verified
- [ ] Build succeeds: `npm run build`
- [ ] No console errors
- [ ] Responsive design tested
- [ ] Dark mode tested
- [ ] API endpoints tested
- [ ] Error states tested
- [ ] Performance profiled
- [ ] Accessibility audited

## Future Architecture Improvements

1. **State Management**: Redux/Zustand for complex state
2. **Query Caching**: React Query for API caching
3. **Real-time Updates**: WebSocket for live results
4. **Offline Support**: Service Workers
5. **Analytics**: Event tracking
6. **Error Tracking**: Sentry integration
