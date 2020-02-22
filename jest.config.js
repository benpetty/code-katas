module.exports = {
  collectCoverage: true,
  collectCoverageFrom: ['katas/**/*.js'],
  coverageDirectory: './coverage',
  coverageReporters: ['text', 'json'],
  moduleDirectories: ['node_modules', 'katas'],
  verbose: true,
  roots: ['<rootDir>/katas/'],
};
