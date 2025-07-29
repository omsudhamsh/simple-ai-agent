# Simple Chat AI Agent

![AI Agent](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

A Level 1 Conversational AI Assistant powered by Google's Gemini 1.5 Flash model. This simple yet elegant chat interface provides an intuitive way to interact with advanced AI capabilities.

## ✨ Features

- 🤖 **Advanced AI**: Powered by Google Gemini 1.5 Flash
- 💬 **Chat Interface**: Clean, modern chat UI
- 🎨 **Beautiful Design**: Product Sans font with gradient styling
- 🌓 **Theme Support**: Automatic dark/light mode adaptation
- 📱 **Responsive**: Works on desktop and mobile devices

## 🚀 Live Demo

[Visit the Live App](https://simple-ai-agent.streamlit.app/) <!-- Add your deployment URL here -->

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/omsudhamsh/simple-ai-agent.git
   cd simple-ai-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Create a `.streamlit/secrets.toml` file
   - Add your Gemini API key:
     ```toml
     GEMINI_API_KEY = "your-api-key-here"
     ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## 🔑 Getting a Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and add it to your `secrets.toml` file

## 📁 Project Structure

```
simple-ai-agent/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── Source/               # Assets folder
│   └── 25231.png        # GitHub logo
├── .streamlit/          # Streamlit configuration
│   └── secrets.toml     # API keys (not in repo)
└── README.md           # This file
```

## 🌐 Deployment

### Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Add your `GEMINI_API_KEY` in the secrets section

### Other Options
- **Heroku**: Add `setup.sh` and `Procfile`
- **Railway**: Direct deployment from GitHub
- **Render**: Connect GitHub and deploy

## 🔒 Security Notes

- ✅ API keys are stored in `secrets.toml` (not tracked by git)
- ✅ Environment variables used in deployment
- ✅ No hardcoded credentials in source code

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini for the powerful AI model
- Streamlit for the amazing web framework
- Product Sans font for beautiful typography

---

**Level 1 - Conversational AI Assistant** ✨ Powered by Gemini 1.5 Flash
