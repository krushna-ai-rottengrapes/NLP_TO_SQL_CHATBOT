# Quick Start Guide

## Prerequisites
- Node.js 18+
- Backend running on http://127.0.0.1:8000

## Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Visit http://localhost:3000

## Usage

1. **Ask a Question**: Type a natural language question in the chat input
2. **View SQL**: The generated SQL appears in the chat with syntax highlighting
3. **See Results**: Results auto-display in the right panel
4. **Interact with Data**:
   - Sort columns by clicking headers
   - Search with the search box
   - Paginate through results
   - Download as CSV
5. **Re-execute**: Click "Re-execute Query" on any previous message

## Troubleshooting

### Backend Connection Error
- Ensure backend is running: `python main.py` in `/backend`
- Check backend is on port 8000
- Check browser console for CORS errors

### No Results Showing
- Check browser console for API errors
- Verify SQL query is valid
- Check backend logs

### Styling Issues
- Clear `.next` folder: `rm -rf .next`
- Rebuild: `npm run build`

## Development

### Add New Component
```bash
# Create in src/app/components/
touch src/app/components/MyComponent.jsx
```

### Add New Hook
```bash
# Create in src/app/hooks/
touch src/app/hooks/useMyHook.js
```

### Modify Styles
Edit `src/app/globals.css` for global styles or use Tailwind classes inline.

## Production Build

```bash
npm run build
npm start
```

The app will be optimized and ready for deployment.
