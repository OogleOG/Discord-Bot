module.exports = {
  apps: [{
    name: 'WeenieBot',
    script: './main.py',
    interpreter: 'python3',
    instances: 1,
    exec_mode: 'fork',
    
    // Auto restart on crash
    autorestart: true,
    watch: false,
    max_memory_restart: '500M',
    
    // Logging
    log_date_format: 'YYYY-MM-DD HH:mm:ss Z',
    out_file: 'logs/pm2_out.log',
    err_file: 'logs/pm2_error.log',
    combine_logs: true,
    
    // Environment
    env: {
      NODE_ENV: 'production'
    },
    
    // Graceful shutdown
    kill_timeout: 10000,
    listen_timeout: 10000,
    shutdown_with_message: true
  }]
};
