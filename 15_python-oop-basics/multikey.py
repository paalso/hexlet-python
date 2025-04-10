# https://ru.hexlet.io/challenges/python_oop_basics_multikey_dictionary_exercise/instance
# https://ru.hexlet.io/code_reviews/1130510


class MultiKeyDict:
    def __init__(self, **kwargs):
        self.vault = {**kwargs}
        self.alias_primary_keys = {}
        self.aliases = {}

    def alias(self, **kwargs):
        for another_key, key in kwargs.items():
            primary_key = self._get_primary_key(key)

            if primary_key is None:
                raise KeyError(f"Key '{key}' not found in vault.")
            
            if another_key in self.vault:
                self._rearrange_keys(another_key, primary_key)
            else:
                current_alias_primary_key = self.alias_primary_keys.get(another_key)
                if current_alias_primary_key:
                    self.aliases[current_alias_primary_key].remove(another_key)
            self.aliases.setdefault(primary_key, set()).add(another_key)
            self.alias_primary_keys[another_key] = primary_key

    @property
    def info(self):
        return f"vault: {self.vault}\nalias_primary_keys: {self.alias_primary_keys}\naliases: {self.aliases}"

    def print_info(self):
        print(self.info)

    def __getitem__(self, key):
        primary_key = self._get_primary_key(key)
        if primary_key is None:
            raise KeyError(f"Key '{key}' not found.")
        return self.vault[primary_key]

    def __setitem__(self, key, value):
        primary_key = self._get_primary_key(key) or key
        self.vault[primary_key] = value

    def _get_primary_key(self, alias):
        if alias in self.vault:
            return alias
        return self.alias_primary_keys.get(alias)

    def _rearrange_keys(self, another_key, primary_key):
        print(f"Rearranging keys: Both primary_key: {primary_key} and another_key: {another_key} are 'primary' keys")
        another_key_aliases = self.aliases[another_key]
        try:
            new_primary_key = another_key_aliases.pop()
            for alias in another_key_aliases:
                self.alias_primary_keys[alias] = new_primary_key
                self.aliases.setdefault(new_primary_key, set()).add(alias)
            self.aliases.pop(another_key)
        except:
            raise
