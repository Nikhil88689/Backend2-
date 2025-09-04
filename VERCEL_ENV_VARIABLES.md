# Environment Variables for Vercel Deployment
# Add these in your Vercel Dashboard under Project Settings > Environment Variables

# Required Environment Variables:
SECRET_KEY=your-secure-secret-key-for-jwt-tokens-at-least-32-characters-long
DATABASE_URL=sqlite:////tmp/notes.db

# Optional (for production with PostgreSQL):
# DATABASE_URL=postgresql://username:password@host:port/database

# Note: VERCEL=1 is automatically set by Vercel