var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync');
var uglify = require('gulp-uglify');
var useref = require('gulp-useref');
var cssnano = require('gulp-cssnano');
var runSequence = require('run-sequence');

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
            baseDir: 'app'
        }
    })
})

gulp.task('sass', function() {
    return gulp.src('app/styles/sass/**/*.scss') // Gets all files ending with .scss in app/scss and children dirs
        .pipe(sass().on('error', sass.logError)) // Passes it through a gulp-sass, log errors to console
        .pipe(gulp.dest('app/styles/css')) // Outputs it in the css folder
        .pipe(browserSync.reload({ // Reloading with Browser Sync
            stream: true
        }));
})

// Watchers
gulp.task('watch', function() {
    gulp.watch('app//styles/sass/**/*.scss', ['sass']);
    gulp.watch('app/**/*.html', browserSync.reload);
    gulp.watch('app/js/**/*.js', browserSync.reload);
})

// Optimization Tasks 
// ------------------

// Optimizing CSS and JavaScript 
gulp.task('useref', function() {

    return gulp.src('app/*.html')
        .pipe(useref())
        .pipe(gulpIf('*.js', uglify()))
        .pipe(gulpIf('*.css', cssnano()))
        .pipe(gulp.dest('dist'));
});

// Build Sequences
// ---------------

gulp.task('default', function(callback) {
    runSequence(['sass', 'browserSync'], 'watch',
        callback
    )
})

gulp.task('build', function(callback) {
    runSequence(
        ['sass', 'useref'],
        callback
    )
})