### 1.cre_singleton_config.py

- An application reads configuration from a file once and all parts of the app must read the same settings.
- Note: The metaclass holds instances per subclass, is thread-safe, and ignores subsequent constructor args (common Singleton caveat).

### 1.cre_singleton_logging.py

- A centralized logging facility that configures formatting/handlers once and modules fetch the same logger instance.

## ---------------------
