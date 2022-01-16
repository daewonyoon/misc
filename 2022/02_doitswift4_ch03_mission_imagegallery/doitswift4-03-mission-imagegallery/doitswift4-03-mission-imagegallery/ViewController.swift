//
//  ViewController.swift
//  doitswift4-03-mission-imagegallery
//
//  Created by Daewon YOON on 2022/01/16.
//

import UIKit

class ViewController: UIViewController {
    
    var imgs = [UIImage]()
    var idx = 0

    @IBOutlet var imgView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        for i in 1...6 {
            imgs.append(UIImage(named: "\(i).png")!)
        }
        
        imgView.image = imgs[idx]
    }


    @IBAction func btnPrevious(_ sender: UIButton) {
        if idx != 0 {
            idx -= 1
            imgView.image = imgs[idx]
        }
    }
    @IBAction func btnNextImage(_ sender: UIButton) {
        if idx != 5 {
            idx += 1
            imgView.image = imgs[idx]
        }
    }
}

