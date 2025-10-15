import { motion } from 'framer-motion';
import { Shield, Brain, Zap, Lock, Code, Database } from 'lucide-react';

export default function About() {
  const features = [
    {
      icon: Shield,
      title: 'Advanced Protection',
      description: 'Uses cutting-edge machine learning algorithms to identify phishing websites with high accuracy.',
    },
    {
      icon: Brain,
      title: 'Multiple ML Models',
      description: 'Choose from Logistic Regression, Random Forest, or Decision Tree models for analysis.',
    },
    {
      icon: Zap,
      title: 'Real-time Analysis',
      description: 'Get instant results with our optimized prediction pipeline and fast API response times.',
    },
    {
      icon: Lock,
      title: 'Privacy Focused',
      description: 'Your URLs are analyzed securely without storing sensitive information.',
    },
  ];

  const technologies = [
    { name: 'Machine Learning', icon: Brain, desc: 'Scikit-learn models' },
    { name: 'Feature Extraction', icon: Database, desc: 'URL analysis' },
    { name: 'Flask API', icon: Code, desc: 'Robust backend service' },
    { name: 'React + Vite', icon: Zap, desc: 'Modern frontend' },
  ];

  return (
    <div className="min-h-screen py-12 bg-gradient-to-br from-blue-50 via-white to-teal-50 dark:from-gray-900 dark:via-gray-900 dark:to-blue-900/20">
      <div className="max-w-6xl px-4 mx-auto sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-16 text-center"
        >
          <h1 className="mb-4 text-5xl font-bold text-transparent bg-gradient-to-r from-blue-600 to-teal-600 dark:from-blue-400 dark:to-teal-400 bg-clip-text">
            About This Project
          </h1>
          <p className="max-w-3xl mx-auto text-xl text-gray-600 dark:text-gray-400">
            A comprehensive phishing detection system powered by machine learning and modern web technologies
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="p-8 mb-16 border border-gray-200 shadow-xl rounded-2xl bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl dark:border-gray-700"
        >
          <h2 className="mb-6 text-3xl font-bold text-gray-900 dark:text-white">
            Purpose & Mission
          </h2>
          <div className="space-y-4 text-lg text-gray-700 dark:text-gray-300">
            <p>
              Phishing attacks remain one of the most common and dangerous cyber threats. Our Phishing Website Detector
              aims to protect users by leveraging advanced machine learning techniques to identify malicious websites
              before they can cause harm.
            </p>
            <p>
              This tool analyzes URL patterns, domain characteristics, and other features to determine whether a
              website is legitimate or a potential phishing attempt. By providing instant analysis through an
              intuitive interface, we empower users to make informed decisions about their online safety.
            </p>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="mb-16"
        >
          <h2 className="mb-8 text-3xl font-bold text-center text-gray-900 dark:text-white">
            Key Features
          </h2>
          <div className="grid gap-6 md:grid-cols-2">
            {features.map((feature, idx) => (
              <motion.div
                key={idx}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.3 + idx * 0.1 }}
                className="p-6 transition-shadow border border-gray-200 shadow-lg rounded-2xl bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl dark:border-gray-700 hover:shadow-xl"
              >
                <div className="flex items-center justify-center w-12 h-12 mb-4 rounded-xl bg-gradient-to-br from-blue-600 to-teal-600">
                  <feature.icon className="w-6 h-6 text-white" />
                </div>
                <h3 className="mb-2 text-xl font-bold text-gray-900 dark:text-white">
                  {feature.title}
                </h3>
                <p className="text-gray-600 dark:text-gray-400">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="p-8 mb-16 border border-blue-200 shadow-xl rounded-2xl bg-gradient-to-br from-blue-100 to-teal-100 dark:from-blue-900/30 dark:to-teal-900/30 backdrop-blur-xl dark:border-blue-800"
        >
          <h2 className="mb-6 text-3xl font-bold text-gray-900 dark:text-white">
            How It Works
          </h2>
          <div className="space-y-4">
            <div className="flex items-start gap-4">
              <div className="flex items-center justify-center flex-shrink-0 w-8 h-8 font-bold text-white bg-blue-600 rounded-full">
                1
              </div>
              <div>
                <h3 className="mb-1 text-lg font-semibold text-gray-900 dark:text-white">
                  URL Submission
                </h3>
                <p className="text-gray-700 dark:text-gray-300">
                  Enter the website URL you want to check into our analysis system.
                </p>
              </div>
            </div>
            <div className="flex items-start gap-4">
              <div className="flex items-center justify-center flex-shrink-0 w-8 h-8 font-bold text-white bg-blue-600 rounded-full">
                2
              </div>
              <div>
                <h3 className="mb-1 text-lg font-semibold text-gray-900 dark:text-white">
                  Feature Extraction
                </h3>
                <p className="text-gray-700 dark:text-gray-300">
                  Our system extracts various features from the URL including length, special characters, domain age,
                  and suspicious patterns.
                </p>
              </div>
            </div>
            <div className="flex items-start gap-4">
              <div className="flex items-center justify-center flex-shrink-0 w-8 h-8 font-bold text-white bg-blue-600 rounded-full">
                3
              </div>
              <div>
                <h3 className="mb-1 text-lg font-semibold text-gray-900 dark:text-white">
                  ML Model Analysis
                </h3>
                <p className="text-gray-700 dark:text-gray-300">
                  Your chosen machine learning model analyzes the extracted features to make a prediction.
                </p>
              </div>
            </div>
            <div className="flex items-start gap-4">
              <div className="flex items-center justify-center flex-shrink-0 w-8 h-8 font-bold text-white bg-blue-600 rounded-full">
                4
              </div>
              <div>
                <h3 className="mb-1 text-lg font-semibold text-gray-900 dark:text-white">
                  Results & Recommendations
                </h3>
                <p className="text-gray-700 dark:text-gray-300">
                  Receive instant results with confidence scores and safety recommendations.
                </p>
              </div>
            </div>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5 }}
          className="mb-16"
        >
          <h2 className="mb-8 text-3xl font-bold text-center text-gray-900 dark:text-white">
            Technologies Used
          </h2>
          <div className="grid gap-6 md:grid-cols-4">
            {technologies.map((tech, idx) => (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.6 + idx * 0.1 }}
                className="p-6 text-center border border-gray-200 shadow-lg rounded-2xl bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl dark:border-gray-700"
              >
                <div className="flex items-center justify-center w-16 h-16 mx-auto mb-4 rounded-xl bg-gradient-to-br from-blue-600 to-teal-600">
                  <tech.icon className="w-8 h-8 text-white" />
                </div>
                <h3 className="mb-1 font-bold text-gray-900 dark:text-white">{tech.name}</h3>
                <p className="text-sm text-gray-600 dark:text-gray-400">{tech.desc}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.7 }}
          className="p-8 text-center border border-gray-200 shadow-xl rounded-2xl bg-white/60 dark:bg-gray-800/60 backdrop-blur-xl dark:border-gray-700"
        >
          <h2 className="mb-4 text-2xl font-bold text-gray-900 dark:text-white">
            Credits & Development
          </h2>
          <p className="mb-4 text-lg text-gray-700 dark:text-gray-300">
            This project was developed to demonstrate the practical application of machine learning in cybersecurity.
          </p>
          <p className="text-gray-600 dark:text-gray-400">
            Built with passion for protecting users from online threats.
          </p>
        </motion.div>
      </div>
    </div>
  );
}
