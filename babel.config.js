module.exports = function(api) {
  api.cache(true);
  const presets = [
    ['@babel/preset-env', {
      useBuiltIns: 'entry',
      corejs: 3,
    }],
  ];

  const plugins = [
    '@babel/plugin-proposal-class-properties',
    '@babel/plugin-transform-strict-mode',
  ];

  return {
    presets,
    plugins,
  };
};
