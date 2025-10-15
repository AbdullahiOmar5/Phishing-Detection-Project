import { motion } from 'framer-motion';
import { Shield, AlertTriangle, CheckCircle, XCircle } from 'lucide-react';

interface EvaluationCardProps {
  result: 'phishing' | 'legitimate' | null;
  confidence?: number;
  url?: string;
}

export default function EvaluationCard({ result, confidence, url }: EvaluationCardProps) {
  if (!result) return null;

  const isPhishing = result === 'phishing';

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9, y: 20 }}
      animate={{ opacity: 1, scale: 1, y: 0 }}
      transition={{ type: 'spring', duration: 0.6 }}
      className={`p-8 rounded-2xl backdrop-blur-xl border-2 shadow-2xl ${
        isPhishing
          ? 'bg-red-50/60 dark:bg-red-900/20 border-red-300 dark:border-red-800'
          : 'bg-green-50/60 dark:bg-green-900/20 border-green-300 dark:border-green-800'
      }`}
    >
      <div className="flex items-center justify-center mb-6">
        <motion.div
          initial={{ scale: 0, rotate: -180 }}
          animate={{ scale: 1, rotate: 0 }}
          transition={{ delay: 0.2, type: 'spring', stiffness: 200 }}
          className={`w-20 h-20 rounded-full flex items-center justify-center ${
            isPhishing
              ? 'bg-red-100 dark:bg-red-900/40'
              : 'bg-green-100 dark:bg-green-900/40'
          }`}
        >
          {isPhishing ? (
            <AlertTriangle className="w-10 h-10 text-red-600 dark:text-red-400" />
          ) : (
            <Shield className="w-10 h-10 text-green-600 dark:text-green-400" />
          )}
        </motion.div>
      </div>

      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="text-center"
      >
        <h3
          className={`text-3xl font-bold mb-2 ${
            isPhishing
              ? 'text-red-700 dark:text-red-400'
              : 'text-green-700 dark:text-green-400'
          }`}
        >
          {isPhishing ? 'Phishing Detected!' : 'Website is Legitimate'}
        </h3>

        <p className="text-gray-600 dark:text-gray-400 mb-4">
          {isPhishing
            ? 'This website appears to be malicious. Avoid entering sensitive information.'
            : 'This website appears to be safe. However, always exercise caution online.'}
        </p>

        {url && (
          <div className="p-3 rounded-lg bg-white/50 dark:bg-gray-800/50 mb-4">
            <p className="text-sm text-gray-700 dark:text-gray-300 break-all">{url}</p>
          </div>
        )}

        {confidence !== undefined && (
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4 }}
            className="mt-4 p-4 rounded-xl bg-white/50 dark:bg-gray-800/50"
          >
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
                Confidence Level
              </span>
              <span className="text-lg font-bold text-gray-900 dark:text-white">
                {confidence}%
              </span>
            </div>
            <div className="w-full h-2 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
              <motion.div
                initial={{ width: 0 }}
                animate={{ width: `${confidence}%` }}
                transition={{ delay: 0.5, duration: 0.8 }}
                className={`h-full rounded-full ${
                  isPhishing
                    ? 'bg-gradient-to-r from-red-500 to-red-600'
                    : 'bg-gradient-to-r from-green-500 to-green-600'
                }`}
              />
            </div>
          </motion.div>
        )}
      </motion.div>

      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="mt-6 flex items-start gap-3 p-4 rounded-lg bg-white/50 dark:bg-gray-800/50"
      >
        {isPhishing ? (
          <XCircle className="w-5 h-5 text-red-600 dark:text-red-400 flex-shrink-0 mt-0.5" />
        ) : (
          <CheckCircle className="w-5 h-5 text-green-600 dark:text-green-400 flex-shrink-0 mt-0.5" />
        )}
        <div className="text-sm text-gray-700 dark:text-gray-300">
          <p className="font-medium mb-1">
            {isPhishing ? 'Safety Recommendations:' : 'Best Practices:'}
          </p>
          <ul className="list-disc list-inside space-y-1 text-gray-600 dark:text-gray-400">
            {isPhishing ? (
              <>
                <li>Do not enter passwords or personal information</li>
                <li>Close this website immediately</li>
                <li>Report the website to authorities</li>
              </>
            ) : (
              <>
                <li>Always verify the URL before entering sensitive data</li>
                <li>Look for HTTPS and security indicators</li>
                <li>Keep your browser and antivirus updated</li>
              </>
            )}
          </ul>
        </div>
      </motion.div>
    </motion.div>
  );
}
