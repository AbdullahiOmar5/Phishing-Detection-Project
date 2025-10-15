import { ChevronDown } from 'lucide-react';

interface ModelSelectorProps {
  selectedModel: string;
  onModelChange: (model: string) => void;
}

export default function ModelSelector({ selectedModel, onModelChange }: ModelSelectorProps) {
  const models = [
    { value: 'lr', label: 'Logistic Regression', icon: '📊' },
    { value: 'rf', label: 'Random Forest', icon: '🌲' },
    { value: 'dt', label: 'Decision Tree', icon: '🌳' }
  ];

  return (
    <div className="relative">
      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
        Select ML Model
      </label>
      <div className="relative">
        <select
          value={selectedModel}
          onChange={(e) => onModelChange(e.target.value)}
          className="w-full px-4 py-3 rounded-xl bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white font-medium appearance-none cursor-pointer focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
        >
          {models.map((model) => (
            <option key={model.value} value={model.value}>
              {model.icon} {model.label}
            </option>
          ))}
        </select>
        <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500 pointer-events-none" />
      </div>
    </div>
  );
}
