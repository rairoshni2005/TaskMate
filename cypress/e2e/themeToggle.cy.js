describe('Theme Toggle', () => {

    it('should toggle theme', () => {

        cy.visit('http://127.0.0.1:5001')

        cy.get('#theme-toggle').click()

    })
})