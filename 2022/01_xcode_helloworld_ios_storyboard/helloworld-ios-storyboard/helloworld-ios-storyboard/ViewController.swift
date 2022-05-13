//
//  ViewController.swift
//  helloworld-ios-storyboard
//
//  Created by Daewon YOON on 2022/01/16.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var titile: UILabel!
    @IBOutlet weak var scream: UILabel!
    @IBOutlet weak var txtName: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func btnSend(_ sender: UIButton) {
        
        titile.text = "Hello, " + txtName.text!
    }
    
}

