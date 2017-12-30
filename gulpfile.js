var gulp = require('gulp');
var gulpif = require('gulp-if');
var sass = require('gulp-sass');
var browserSync = require('browser-sync');
var minifyjs = require('gulp-js-minify');
var cssnano = require('gulp-cssnano');
var runSequence = require('run-sequence');
var htmlmin = require('gulp-htmlmin');
var imageop = require('gulp-image-optimization');
var uglify = require('gulp-uglify');
var pump = require('pump');

// Basic Gulp task syntax
gulp.task('hello', function() {
    console.log('Eshta Ya Me3allemm!');
})

// Development Tasks 
// -----------------

// Start browserSync server
gulp.task('browserSync', function() {
    browserSync({
        server: {
            baseDir: 'docs'
        }
    })
})

gulp.task('sass', function() {
    return gulp.src('docs/styles/sass/**/*.scss') // Gets all files ending with .scss in docs/scss and children dirs
        .pipe(sass().on('error', sass.logError)) // Passes it through a gulp-sass, log errors to console
        .pipe(gulp.dest('docs/styles/css')) // Outputs it in the css folder
        .pipe(browserSync.reload({ // Reloading with Browser Sync
            stream: true
        }));
})

// Watchers
gulp.task('watch', function() {
    gulp.watch('docs/styles/sass/**/*.scss', ['sass']);
    gulp.watch('docs/**/*.html', browserSync.reload);
    gulp.watch('docs/js/**/*.js', browserSync.reload);
})

// Optimization Tasks 
// ------------------

// Optimizing CSS and JavaScript 
// gulp.task('js-minify', function() {
//     return gulp.src('docs/js/*.js')
//     .pipe(minifyjs())
//     .pipe(gulp.dest('dist/js/'));
// });

gulp.task('js-minify', function (cb) {
    pump([
          gulp.src('docs/js/*.js'),
          uglify(),
          gulp.dest('amazon/js/')
      ],
      cb
    );
  });

gulp.task('css-minify', function() {
    return gulp.src('docs/styles/css/**/*.css')
        .pipe(cssnano())
        .pipe(gulp.dest('amazon/css/'));
});

gulp.task('img-minify', function(cb) {
    gulp.src('docs/**/*.+(png|jpg|gif|jpeg)').pipe(imageop({
        optimizationLevel: 5,
        progressive: true,
        interlaced: true
    })).pipe(gulp.dest('dist/img')).on('end', cb).on('error', cb);
});

//Minify html
gulp.task('minify', function() {
    return gulp.src('docs/**/*.html')
      .pipe(htmlmin({collapseWhitespace: true}))
      .pipe(gulp.dest('amazon'));
  });

// Copy files for prod
gulp.task('amazon', function(){
    return gulp.src(['docs/**/*.html', '!docs/**/_*/', '!docs/**/_*/**/*', 'docs/**/*.css', 'docs/**/*.js', 'dist/**/*.png', 'docs/*fonts/**'])
    .pipe(gulp.dest('amazon'))
});

// Build Sequences
// ---------------

gulp.task('default', function(callback) {
    runSequence(['hello', 'sass', 'browserSync'], 'watch',
        callback
    )
})

gulp.task('build', function(callback) {
    runSequence(
        ['sass', 'js-minify', 'css-minify', 'minify'],
        callback
    )
})