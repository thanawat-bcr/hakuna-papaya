module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/essential',
    '@vue/airbnb',
    '@vue/typescript/recommended',
  ],
  parserOptions: {
    ecmaVersion: 2020,
  },
  rules: {
    'no-console': 'off',
    'no-debugger': 'off',
    'max-len': 'off',
    'no-underscore-dangle': 'off',
    '@typescript-eslint/no-namespace': 'off',
    'import/no-extraneous-dependencies': 'off',
    'import/no-cycle': 'off',
  },

};
