/**
 * @file Babel Project-wide configuration file
 * @summary https://babeljs.io/docs/en/config-files#project-wide-configuration
 */

/**
 * JS config files may export a function that will be passed config function API:
 * https://babeljs.io/docs/en/config-files#config-function-api
 */
module.exports = function(api) {

  // https://babeljs.io/docs/en/config-files#apicache
  api.cache(true);

  // Don't want to assemble your own set of plugins? No problem! Presets can
  // act as an array of Babel plugins or even a sharable options config.
  // https://babeljs.io/docs/en/presets
  const presets = [

    // @babel/preset-env is a smart preset that allows you to use the
    // latest JavaScript without needing to micromanage which syntax
    // transforms (and optionally, browser polyfills) are needed by
    // your target environment(s). This both makes your life easier and
    // JavaScript bundles smaller!
    // https://babeljs.io/docs/en/babel-preset-env
    ['@babel/preset-env', {
      // This option adds direct references to the core-js module as
      // bare imports. Thus core-js will be resolved relative to the
      // file itself and needs to be accessible. You may need to
      // specify core-js@3 as a top level dependency in your
      // application if there isn't a core-js dependency or there are
      // multiple versions.
      // "usage" | "entry" | false, defaults to false.
      // https://babeljs.io/docs/en/babel-preset-env#usebuiltins
      useBuiltIns: 'entry',

      // This option only has an effect when used alongside useBuiltIns: usage or
      // useBuiltIns: entry, and ensures @babel/preset-env injects the correct
      // imports for your core-js version.
      // https://babeljs.io/docs/en/babel-preset-env#corejs
      corejs: 3,
    }],
  ];

  const plugins = [

    // This plugin transforms static class properties as well as properties
    // declared with the property initializer syntax
    // https://babeljs.io/docs/en/next/babel-plugin-proposal-class-properties.html
    '@babel/plugin-proposal-class-properties',

    // This plugin may be enabled via @babel/plugin-transform-modules-commonjs.
    // If you wish to disable it you can either turn strict off or pass
    // strictMode: false as an option to the commonjs transform.
    // https://babeljs.io/docs/en/babel-plugin-transform-strict-mode/
    '@babel/plugin-transform-strict-mode',

  ];

  return {
    presets,
    plugins,
  };
};