# NLP → SQL Studio - Frontend Implementation

## 🎯 Overview

Production-grade Next.js frontend for converting natural language queries to SQL with a modern, responsive two-pane layout inspired by VS Code.

## 📁 Project Structure

```
src/app/
├── components/
│   ├── Navbar.jsx           # Sticky navbar with theme toggle
│   ├── ChatPanel.jsx        # Chat interface with message history
│   ├── ChatMessage.jsx      # Individual message with SQL syntax highlighting
│   ├── ResultPanel.jsx      # Results display (KPI cards or data table)
│   ├── DataTable.jsx        # Advanced data table with sorting/pagination
│   └── KPICard.jsx          # Single-value result card
├── hooks/
│   ├── useTheme.js          # Theme management with localStorage
│   └── useApi.js            # API integration for query/execute endpoints
├── page.js                  # Main layout with resizable panels
├── layout.js                # Root layout with metadata
└── globals.css              # Design tokens and global styles
```

## 🎨 Design Decisions

### 1. **Two-Pane Resizable Layout**
- Used `react-resizable-panels` for VS Code-like experience
- Smooth drag-to-resize with visual feedback
- Responsive breakpoints: 30% minimum width per panel
- Hover effect on divider for discoverability

### 2. **Color & Typography**
- **Amazon-inspired palette**: Neutral grays with blue accents
- **Dark mode**: Full support with CSS variables
- **Typography**: System fonts for performance (no external font loading)
- **Spacing**: 4px grid system via Tailwind

### 3. **Component Architecture**
- **Functional components** with React hooks
- **Separation of concerns**: UI, logic, API calls
- **Reusable hooks**: `useTheme`, `useApi` for state management
- **No prop drilling**: Direct API calls in components

### 4. **Data Display Strategy**

**Single-value results** (COUNT, SUM, etc.):
- KPI card with large typography
- Hover glow effect for visual feedback
- Number formatting with locale support

**Multi-row results**:
- TanStack Table for enterprise-grade features
- Sticky header for scrolling
- Sorting, pagination, search, CSV export
- Responsive column sizing

### 5. **Chat Experience**
- Message history maintained in state
- Auto-scroll to latest message
- SQL syntax highlighting with `react-syntax-highlighter`
- Copy-to-clipboard button with visual feedback
- Re-execute previous queries with one click

### 6. **Loading & Error States**
- Spinner during API calls
- Error boundaries with user-friendly messages
- Disabled states on buttons during loading
- Graceful fallbacks for empty states

## 🔧 Technology Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Framework | Next.js 16 | Server components, built-in optimization |
| UI Library | React 19 | Latest hooks, concurrent features |
| Styling | Tailwind CSS 4 | Utility-first, dark mode support |
| Icons | Lucide React | Lightweight, tree-shakeable |
| Tables | TanStack Table | Headless, feature-rich, no bloat |
| Syntax Highlighting | react-syntax-highlighter | SQL support, theme customization |
| Resizable Panels | react-resizable-panels | Smooth, accessible, performant |
| CSV Export | PapaParse | Lightweight, reliable |

## 🚀 Getting Started

### Installation
```bash
cd frontend
npm install
```

### Development
```bash
npm run dev
```
Open http://localhost:3000

### Build
```bash
npm run build
npm start
```

## 📡 API Integration

### Query Endpoint
```
POST http://127.0.0.1:8000/database/query
Body: { "question": "string" }
Response: {
  "status": "success",
  "question": "string",
  "sql_query": "string",
  "filtered_tables": ["string"],
  "schema_token_size": number
}
```

### Execute Endpoint
```
POST http://127.0.0.1:8000/database/execute-sql
Body: { "sql_query": "string" }
Response: {
  "status": "success",
  "data": [{ ... }],
  "columns": ["string"]
}
```

## 🎯 Features Implemented

✅ Sticky navbar with theme toggle  
✅ Resizable two-pane layout  
✅ Chat interface with message history  
✅ SQL syntax highlighting  
✅ Copy SQL to clipboard  
✅ Re-execute previous queries  
✅ KPI card display for single values  
✅ Advanced data table with sorting/pagination/search  
✅ CSV export  
✅ Floating action button (Talk to Data)  
✅ Dark mode support  
✅ Responsive design (mobile, tablet, desktop)  
✅ Loading spinners  
✅ Error handling  

## 🎨 Responsive Breakpoints

- **Mobile**: < 640px (single column, stacked layout)
- **Tablet**: 640px - 1024px (optimized spacing)
- **Desktop**: > 1024px (full two-pane layout)

## 🔐 Security & Performance

- No sensitive data in localStorage (only theme preference)
- CORS handled by backend
- Lazy loading of components
- Optimized re-renders with React.memo where needed
- CSS-in-JS minimized (Tailwind purges unused styles)

## 📝 Code Quality

- ESLint configured for Next.js
- Consistent naming conventions
- Minimal comments (code is self-documenting)
- No console.logs in production
- Proper error boundaries

## 🚧 Future Enhancements

- Query history persistence
- Saved queries
- Query templates
- Real-time collaboration
- Advanced filtering UI
- Query performance metrics
- Schema explorer sidebar

## 📞 Support

For issues or questions, check the backend API logs and browser console for debugging.
