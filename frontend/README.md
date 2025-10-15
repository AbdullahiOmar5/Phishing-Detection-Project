# 🕵️‍♂️ Phishing Website Detector – Frontend
A modern React + Vite web application for detecting phishing websites using trained machine learning models (Random Forest, Logistic Regression, and Decision Tree).
This frontend connects seamlessly with a Flask API and delivers a beautiful, fast, and interactive user experience.

## 🌐 URL Input Interface
Single URL Field – Enter any website link for analysis
Real-time Validation – Checks for valid URL format before submission
Model Selection – Choose from three ML models
Instant Predictions – Displays clear “Phishing” or “Legitimate” results
## 📊 Model Options
Model 1: Logistic Regression – 🧠 Simple & fast baseline model
Model 2: Decision Tree – 🌿 Interpretable tree-based classifier
Model 3: Random Forest – ⚡ High-accuracy ensemble model
## 🎨 UI Enhancements
Elegant Navbar – Home, Predict, and About sections
Animated Header – Engaging hero section with a clear project tagline
URL Card Input – Clean prediction form with submit button
Result Visualization – Modern cards showing model predictions and probabilities
Responsive Design – Perfect across desktop, tablet, and mobile
Dark Mode Support – Seamless adaptation to system theme
## 🚀 Quick Start
### Install dependencies
npm install

### Run development server
npm run dev

### Build for production
npm run build

### Preview production build
npm run preview
Then open in your browser:
👉 http://localhost:5173
## 🔗 API Integration
The app communicates with the Flask backend (default: http://127.0.0.1:5000)
Each model can be selected using the query parameter model=lr|rf|dt.
Example Request:
POST http://127.0.0.1:5000/predict?model=rf

{
  "url": "https://paypal-login-secure-update.com/account"
}
Example Response:
{
  "model": "rf",
  "prediction": "Phishing",
  "raw_label": 1,
  "probability_phishing": 0.85,
  "url": "https://paypal-login-secure-update.com/account"
}
## 🧭 Navigation Pages
Page	    Description
🏠 Home	Project introduction, hero section, and CTA buttons
🔍 Predict	URL input card, model selection, and prediction results
ℹ️ About	Explains dataset, ML models, and project overview

## 🛠️ Tech Stack
Layer	Technology
Frontend	React + Vite
Styling	Tailwind CSS + shadcn/ui
Icons	Lucide React
Animation	Framer Motion
Charts (optional)	Recharts
Backend	Flask API
Language	Python (Scikit-Learn, Pandas, Joblib)
## 📱 Responsive Design
The interface is optimized for all devices:
🖥 Desktop: Full layout with animated header and cards
📱 Mobile: Stacked prediction cards with large input buttons
💻 Tablet: Balanced layout with adaptive spacing
## 🎨 Design Highlights
Glassmorphism Cards – Semi-transparent UI with blur effects
Soft Gradients – Subtle modern color transitions
Consistent Icons – Visual cues for actions and results
Hover Animations – Interactive feedback on buttons
Dark/Light Mode Compatibility
