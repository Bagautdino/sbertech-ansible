Vagrant.configure("2") do |config|
  config.vm.provider :utm do |u|
    u.utm_file_url = "https://github.com/naveenrajm7/utm-box/releases/download/debian-11/debian_vagrant_utm.zip"
    u.directory_share_mode = "webDAV"
    u.check_guest_additions = false
  end

  config.vm.synced_folder ".", "/vagrant", create: true
  config.ssh.username = "debian"
  config.ssh.insert_key = true

  # Проброс порта SSH для доступа Ansible
  config.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh"

  # Провиженинг с использованием Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbooks/site.yml"
    ansible.verbose = "vvv"
  end
end
