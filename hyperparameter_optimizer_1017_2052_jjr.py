# 代码生成时间: 2025-10-17 20:52:41
import requests

class HyperparameterOptimizer:
    def __init__(self, base_url):
        """
        Initializes the optimizer with the base URL of the API.
        """
        self.base_url = base_url

    def optimize(self, parameters, loss_function, n_iterations=100):
        """
        Performs hyperparameter optimization by calling the API.
        
        :param parameters: A dictionary of hyperparameters to optimize.
        :param loss_function: The loss function to minimize.
        :param n_iterations: The number of iterations to perform.
        :return: A dictionary with the optimized hyperparameters.
        """
        best_params = None
        best_loss = float('inf')
        for _ in range(n_iterations):
            # Randomly sample a set of hyperparameters
            trial_params = self._sample_hyperparameters(parameters)
            # Send the trial parameters to the API to calculate loss
            response = requests.post(f"{self.base_url}/evaluate", json=trial_params)
            if response.status_code != 200:
                print(f"Error: {response.text}")
                continue
            loss = response.json().get('loss', float('inf'))
            # Update the best parameters if the current loss is better
            if loss < best_loss:
                best_loss = loss
                best_params = trial_params
        return best_params

    def _sample_hyperparameters(self, parameters):
        """
        Samples a random set of hyperparameters from the given range.
        """
        sample = {}
        for name, (start, end) in parameters.items():
            sample[name] = start + (end - start) * np.random.random()
        return sample

# Usage example
if __name__ == '__main__':
    optimizer = HyperparameterOptimizer("http://api.example.com")
    parameters = {
        'learning_rate': (0.001, 0.1),
        'batch_size': (16, 256),
        'epochs': (10, 100)
    }
    optimized_params = optimizer.optimize(parameters, 'cross_entropy_loss')
    print(f"Optimized parameters: {optimized_params}")
